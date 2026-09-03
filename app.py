from flask import Flask,request
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from models import db,Librarian

#create the flask app
app=Flask(__name__)
#configure the database
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///library.db"
db.init_app(app)#db+init=>connected
migrate=Migrate(app,db)
ma=Marshmallow(app)

@app.route("/librarians",methods=["GET"] )
def get_librarians():
	from schemas import LibrarianSchema
	librarians=db.session.execute(db.select(Librarian)).scalars().all()
	librarians_schema=LibrarianSchema(many=True)
	return librarians_schema.dump(librarians)

@app.route("/librarians",methods=["POST"] )
def create_librarian():
	from schemas import LibrarianSchema
	data=request.get_json()
	schema=LibrarianSchema()
	validated_data=schema.load(data)
	new_librarian=Librarian(name=validated_data["name"],email=validated_data["email"])
	db.session.add(new_librarian)
	db.session.commit()
	return schema.dump(new_librarian),201

if __name__=="__main__":
	app.run(debug=True)