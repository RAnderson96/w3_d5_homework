from flask import render_template, request, redirect
from app import app
from models.library import Library
from models.library_instance import books, add_book_to_list, remove_book_from_list, checkout_book

@app.route('/library')
def index():
    return render_template('index.html', title="CodeClan Library", books=books)
    
@app.route('/library/<index>')
def more_info(index):
    return render_template('detail.html', title="CodeClan Library",  books=books[int(index)-1], index=index)

@app.route('/library', methods=['POST'])
def add_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    book_blurb = request.form["blurb"]
    new_book = Library(book_title, book_author, book_author, book_blurb)
    add_book_to_list(new_book)
    return redirect('/library')

@app.route('/library/delete/<title>', methods=['POST'])
def remove_book(title):
    remove_book_from_list(title)
    return redirect('/library')

@app.route('/library/check_out/<title>', methods=['POST'])
def check_out(title):
    checkout_book(title)
    return redirect('/library') 

    