from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Contributor, Publisher, Review
from .utils import average_rating
from .forms import SearchForm, PublisherForm, ReviewForm

# messages, allows us to register a message letting the user know that a Publisher object was edited or created
from django.contrib import messages

def index(request):
    return render(request, "base.html")

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0

        book_list.append(
            {'book': book,
             'book_rating': book_rating,
             'number of reviews': number_of_reviews}
        )
    context = {
        'book_list': book_list
    }

    return render(request, 'reviews/books_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating(
            [review.rating for review in reviews]
        )
        context = {
            'book': book,
            'book_rating': book_rating,
            'reviews': reviews
        }
    else:
        context = {
            'book': book,
            'book_rating': None,
            'reviews': None
        }
    return render(request, "reviews/book_detail.html", context)

def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    books = set() # Used as a placeholder if the form is not valid

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(first_names__icontains=search)

            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

            lname_contributors = Contributor.objects.filter(last_names__icontains=search)

            for contributor in lname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

    return render(request, "reviews/search-results.html", {"form": form, "search_text": search_text, "books": books})

def publisher_edit(request, pk=None):
    # If we are given a primary key, retrieve that record from the model as an object
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    # If we are not given a primary key, set an empty publisher record
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, f"Publisher {updated_publisher} was created.")
            else:
                messages.success(request, f"Publisher {updated_publisher} was updated.")

            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, 'reviews/instance-form.html',
        {"method": request.method, "form": form, "instance": publisher, "model_type": "Publisher"})

def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    # If the book has a review, retrieve the review for that book (Updating a review)
    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
    # If the book does not have a review, set review to None (Creating a review)
    else:
        review = None

    # POST Branch
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book
            if review is None: # If there was no review for the book
                messages.success(request, f"Review for {book} created.")
            else: # If you updated a review for the book
                updated_review.date_edited = timezone.now()
                messages.success(request, f"Review for {book} updated.")
                updated_review.save()
            return redirect("book_detail", book.pk)
    # Non-POST Branch
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/instance-form.html",
                  {"form": form, "instance": review,
                   "model_type": "Review",
                   "related_instance": book,
                   "related_model_type": "Book"})





























