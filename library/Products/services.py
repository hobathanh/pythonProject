# from library.extension import db
# from library.library_ma import BookSchema
# from library.model import Author, Books, Category
# from flask import request, jsonify
# from sqlalchemy.sql import func
# import json
# book_schema = BookSchema()
# books_schema = BookSchema(many=True)


# def add_book_service():
#     data = request.json
#     if (data and ('name' in data) and ('page_count' in data)
#             and ('author_id' in data) and ('category_id' in data)):
#         name = data['name']
#         page_count = data['page_count']
#         author_id = data['author_id']
#         category_id = data['category_id']
#         try:
#             new_book = Books(name, page_count, author_id, category_id)
#             db.session.add(new_book)
#             db.session.commit()
#             return jsonify({"message": "Add success!"}), 200
#         except IndentationError:
#             db.session.rollback()
#             return jsonify({"message": "Can not add book!"}), 400
#     else:
#         return jsonify({"message": "Request error"}), 400

