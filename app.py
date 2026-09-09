from flask import Flask,request,session
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from models import db,Librarian,User
from flask_bcrypt import Bcrypt

#create the flask app
app=Flask(__name__)
#configure the database
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///library.db"
app.config["SECRET_KEY"]="development-secret-key"
db.init_app(app)#db+init=>connected
migrate=Migrate(app,db)
ma=Marshmallow(app)
bcrypt=Bcrypt(app)

@app.route("/librarians",methods=["GET"] )
def get_librarians():
			page=request.args.get("page",3,type=int)
			per_page=request.args.get("per_page",2,type=int)
			statement=db.select(Librarian).order_by(Librarian.id)
			pagination=db.paginate(statement,page=page,per_page=per_page, error_out=False)
			librarians=pagination.items
			from schemas import LibrarianSchema
			librarians=db.session.execute(db.select(Librarian)).scalars().all()
			librarians_schema=LibrarianSchema(many=True)
			return {
			"librarians":librarians_schema.dump(librarians),	
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "total_pages": pagination.pages
        }, 200

	# GET/books?page=1&per_page=2

@app.route("/librarians",methods=["POST"] )
def create_librarian():
	user_id=session.get("user_id")
	if user_id is None:
		return{
			"error":"Authentication required"
		},401
	from schemas import LibrarianSchema
	data=request.get_json()
	schema=LibrarianSchema()
	validated_data=schema.load(data)
	new_librarian=Librarian(name=validated_data["name"],email=validated_data["email"])
	db.session.add(new_librarian)
	db.session.commit()
	return schema.dump(new_librarian),201

@app.route('/register',methods=["POST"])
def register():
	data=request.get_json()
	existing_user=db.session.execute(
		db.select(User).where(User.email==data["email"])
	).scalar_one_or_none()

	if existing_user:
		return{
			"error":"Email already registered"
		},400
	password_hash=bcrypt.generate_password_hash(data["password"]).decode("utf-8")
	user=User(
		name=data["name"],
		email=data["email"],
		password=password_hash
	)
	db.session.add(user)
	db.session.commit()

	return {
		'message':"User registered successfully"
	},201

@app.route('/login',methods=["POST"])
def login():
	data=request.get_json()
	user=db.session.execute(
		db.select(User).where(User.email==data["email"])
	).scalar_one_or_none()

	if user is None:
		return{
			"error":"Invalid email"
		},401
	
	password_correct=bcrypt.check_password_hash(user.password,data["password"])
	if not password_correct:
		return{
					"error":"Invalid password"
				},401

	session["user_id"]=user.id

	return{
		"message":"Login successful"
	},200
@app.route('/me',methods=["GET"])
def current_user():
	user_id=session.get("user_id")
	if user_id is None:
		return{
			"error":"Not authenticated"
		},401
	user=db.session.get(User,user_id)

	return{
		"id":user.id,
		"name":user.name,
		"email":user.email
	},200
@app.route('/logout',methods=["DELETE"])
def logout():
	session.pop("user_id",None)
	return{
			"message":"Logout successful"
		},200


if __name__=="__main__":
	app.run(debug=True)