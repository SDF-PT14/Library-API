from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# metadata=Metadata()

db=SQLAlchemy()# create sqlalchemy object and store it in db

#Book model
class Book(db.Model):
	__tablename__="books"
	id=db.Column(db.Integer,primary_key=True) #id INTEGER PRIMARY KEY
	title=db.Column(db.String(100),nullable=False) #NOT NULL
	author=db.Column(db.String(100),nullable=False)
	author_id=db.ForeignKey("authors.id", name="fk_books_author_id")
	category=db.Column(db.String(50),nullable=False)
	available=db.Column(db.Boolean,default=True)


class Author(db.Model):
	__tablename__="authors"
	id=db.Column(db.Integer,primary_key=True) #id INTEGER PRIMARY KEY
	name=db.Column(db.String(100),nullable=False) #NOT NULL
	country=db.Column(db.String(100),nullable=False) #NOT NULL
	writer=db.relationship("Author",back_populates="books")
