from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# create sqlalchemy object and store it in db

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata=MetaData(naming_convention=convention)
db=SQLAlchemy(metadata=metadata)

#Book model
class Book(db.Model):
	__tablename__="books"
	id=db.Column(db.Integer,primary_key=True) #id INTEGER PRIMARY KEY
	title=db.Column(db.String(100),nullable=False) #NOT NULL
	author=db.Column(db.String(100),nullable=False)
	category=db.Column(db.String(50),nullable=False)
	available=db.Column(db.Boolean,default=True)
	author_id=db.Column(db.Integer,db.ForeignKey("authors.id"),nullable=True)
	author_details=db.relationship("Author",back_populates="books")


class Author(db.Model):
	__tablename__="authors"
	id=db.Column(db.Integer,primary_key=True) #id INTEGER PRIMARY KEY
	name=db.Column(db.String(100),nullable=False) #NOT NULL
	country=db.Column(db.String(100),nullable=False) #NOT NULL
	books=db.relationship("Book",back_populates="author_details")
	
