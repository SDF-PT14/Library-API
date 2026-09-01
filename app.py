from flask import Flask 
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from models import db
#create the flask app
app=Flask(__name__)

#configure the database
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///library.db"

db.init_app(app)#db+init=>connected

migrate=Migrate(app,db)
ma=Marshmallow(app)
@app.route("/")
def home():
	return {
		"message":"Library API is running "
	}
if __name__=="__main__":
	app.run(debug=True)