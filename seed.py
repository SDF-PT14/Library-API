from app import app
from models import db,Book,Author

with app.app_context():
	chinua=Author(
		name="Chinua Achebe",
		country="Nigeria"
	)
	margaret=Author(
		name="Margaret Ogola",
		country="Kenya"
	)
	nelson=Author(
		name="Nelson Mandela",
		country="South Africa"
	)
	ngugi=Author(
		name="Ngugi",
		country="Kenya"
	)

	db.session.add_all([chinua,margaret,nelson,ngugi])
	db.session.commit()
	book1=db.session.get(Book,1)
	book2=db.session.get(Book,2)
	book3=db.session.get(Book,3)

	book1.author_details=chinua
	book2.author_details=margaret
	book3.author_details=nelson
	db.session.commit()

	print("Authors created and books connected successfully")
		
	# book1=Book(
	# 		title="Things Fall Apart",
	# 		author="chinua",
	# 		category="fiction",

	# 	)
	# book2=Book(
	# 		title="The river and the source",
	# 		author="Margaret",
	# 		category="fiction",

	# 	)
	# book3=Book(
	# 		title="Long Walk to Freedom ",
	# 		author="Nelson  Mandela ",
	# 		category="Biography",

	# 	)
	# db.session.add_all([book1,book2,book3])
	# db.session.commit()
	# print("Books added successfully")
		

		
