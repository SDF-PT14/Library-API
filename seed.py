from app import app
from models import db,Book

with app.app_context():
	book1=Book(
		title="Things Fall Apart",
		author="chinua",
		category="fiction",

	)
	book2=Book(
		title="The river and the source",
		author="Margaret",
		category="fiction",

	)
	book3=Book(
		title="Long Walk to Freedom ",
		author="Nelson  Mandela ",
		category="Biography",

	)
	db.session.add_all([book1,book2,book3])
	db.session.commit()
	print("Books added successfully")
	

	
