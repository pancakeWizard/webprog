from django.shortcuts import render
from . models import *

LIKE_MAPPING = {
    "like" :            1,
    "dislike":          2,
}


def reverse_map(map, value):
    for key, val in map.items():
        if val == value:
            return key
    return None

# Create your views here.
def books(request):
    books = Book.objects.all()
    data = {
        "navBookBtn": True,
        "books": books
    }
    return render(request, 'books.html', data)

def bookRes(request, bookName, bookId):
    user = request.user
    book = Book.objects.get(title=bookName)
    recensions = Recension.objects.filter(book=book)
    print(recensions)
    data = {
        "navBookBtn": True,
        "book": book,
        "recensions":recensions,
    }
    if user.is_authenticated:
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
        user_res_like_status = False
        try:
            user_book_like_status = BookLike.objects.get(user=user, book=book)
            if user_book_like_status:
                data["user_book_like_status"] = user_book_like_status
        except:
            pass 
    return render(request, "bookRes.html", data)