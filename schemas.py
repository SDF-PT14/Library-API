from app import ma

class BookSchema(ma.Schema):
	id=ma.Integer()
	title=ma.String()
	author=ma.String()
	category=ma.String()
	available=ma.Boolean()

class LibraryBranchSchema(ma.Schema):
	id=ma.Integer(dump_only=True)
	name=ma.String()
	location=ma.String()

class LibrarianSchema(ma.Schema):
	id=ma.Integer(dump_only=True)
	name=ma.String(required=True)
	email=ma.String(required=True)
	branches=ma.Nested(LibraryBranchSchema,many=True,dump_only=True)