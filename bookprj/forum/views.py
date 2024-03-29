from django.shortcuts import redirect, render
from . models import *

LIKE_MAPPING = {
    "like_remove":      0,
    "dislike_remove":   0,
    "like" :            1,
    "dislike":          2,
}

def books(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    data = {
        "navBookBtn": True,
        "books": books,
        "authors": authors
    }
    return render(request, 'books.html', data)

def bookRes(request, bookName, bookId):
    user = request.user
    book = Book.objects.get(title=bookName)
    recensions = Recension.objects.filter(book=book)
    data = {
        "navBookBtn": True,
        "book": book,
        "recensions":recensions,
    }
    if user.is_authenticated:
        try:
            cur_user_rec = Recension.objects.get(author=user, book=book)
        except:
            cur_user_rec = False
        print(cur_user_rec)
        if request.method == "POST":
            new_book_like_entry = False
            try:
                user_book_like_status = BookLike.objects.get(user=user, book=book)
            except:
                new_book_like_entry = True
            bookLike = request.POST.get("bookLike")
            
            new_book_like_value = LIKE_MAPPING.get(bookLike, 0)
            if not new_book_like_entry:
                previousValue = user_book_like_status.like
                user_book_like_status.like = new_book_like_value
                user_book_like_status.save()
                book.dislikes -= 1 if previousValue == 2 else 0
                book.dislikes += 1 if user_book_like_status.like == 2 else 0

                book.likes -= 1 if previousValue == 1 else 0
                book.likes += 1 if user_book_like_status.like == 1 else 0
            else:
                user_book_new_like_entry = BookLike(book=book, user=user, like=new_book_like_value)
                user_book_new_like_entry.save()
                book.likes += 1 if bookLike == "like" else 0
                book.dislikes += 1 if bookLike == "dislike" else 0
            book.save()
        try:
            user_book_like_status = BookLike.objects.get(user=user, book=book)
            if user_book_like_status:
                data["user_book_like_status"] = user_book_like_status
        except:
            pass 
        data["cur_user_rec"] = cur_user_rec
    return render(request, "bookRes.html", data)

def bookCreateRes(request, bookName, bookId):
    if request.user.is_authenticated:
        if request.method == "POST":
            recension = request.POST.get("recension")
            book = Book.objects.get(id=bookId)
            try:
                user_res_query = Recension.objects.get(author=request.user, book=book)
            except:
                user_res_query = Recension.objects.create(book=book, author=request.user, recension=recension)
            else:
                user_res_query.recension = recension
            finally:
                user_res_query.save()
    return redirect('bookRes', bookName, bookId)


def authors(request):
    authors = Author.objects.all()
    data = {
        "authors": authors,
        "navAuthorBtn": True
    }
    return render(request, "authors.html", data)

def filterBooks(request):
    authors  = Author.objects.all()
    data = {
        "authors": authors
        }
    if request.method == "POST":
        books = Book.objects.all()
        user_author = request.POST.get("author")
        if user_author:
            author = Author.objects.get(id=user_author)
            books = books.filter(author=author)
            data["books"] = books
            data["navBookBtn"] = True
            return render(request, 'books.html', data)
        search_book_input = request.POST.get("search_book")
        if search_book_input:
            books = books.filter(title__icontains=search_book_input)
            data["books"] = books
            data["navBookBtn"] = True
            return render(request, 'books.html', data)
        search_author_input = request.POST.get("search_author")
        if search_author_input:
            authors = Author.objects.filter(name__icontains=search_author_input)
            data["authors"] = authors
            data["navAuthorBtn"] = True
            return render(request, "authors.html", data)
    return redirect('books')

def author(request, authorName, authorId):
    author = Author.objects.get(id=authorId)
    books = Book.objects.filter(author=author)
    data = {
        "navAuthorBtn": True,
        "author":author,
        "books": books
    }
    return render(request, 'author.html', data)

def add(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            bookTitle = request.POST.get("bookTitle")
            if bookTitle:
                description = request.POST.get("description")
                book_query = Book.objects.create(title=bookTitle, description=description, user=user)
                book_query.save()
                authors_amount = request.POST.get("authorHelper")
                for i in range(int(authors_amount)):
                    bookAuthor = request.POST.get(f"bookAuthor_{i+1}")
                    author = Author.objects.get(name=bookAuthor)
                    book_query.author.add(author)
            else:
                authorName = request.POST.get("authorName")
                try:
                    author = Author.objects.get(name=authorName)
                except:
                    description = request.POST.get("description")
                    author_query = Author.objects.create(name=authorName, description=description)
                    author_query.save()
    return redirect('books')

def deleteRes(request, bookName, bookId):
    if request.method == "POST":
        try:
            res_id = request.POST.get("res_id")
            Recension.objects.get(id=res_id).delete()
        except:
            pass
    
    return redirect('bookRes', bookName, bookId)

def deleteBook(request):
    if request.method == "POST":
        
        bookId = request.POST.get("bookId")
        book = Book.objects.get(id=bookId).delete()

    return redirect('books')
