from app import ma

class BookSchema(ma.Schema):
	id=ma.Integer()
	title=ma.String()
	author=ma.String()
	category=ma.String()
	available=ma.Boolean()
	