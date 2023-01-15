from django.db import models
from django.contrib import auth
class Publisher(models.Model):
    """Used to contain Publisher details
    - Name: CharField, Used to contain the name of the publisher
    - Website: URLField, Used to contain the Publisher's website
    - Email: EmailField, Used to contain the Publisher's email
    """
    name = models.CharField(
        max_length = 50,
        help_text="The name of the Publisher."
    )
    website = models.URLField(
        help_text="The Publisher's website."
    )
    email = models.EmailField(
        help_text="The Publisher's email address."
    )

    def __str__(self):
        return self.name

class Book(models.Model):
    """Contains the information about the Book itself
    - Title: CharField, the title of the book
    - ISBN: CharField, ISBN number of the book
    - Publisher: Foreign Key, The publisher that created the book
    - Contributors: Foreign Key, Contributors to this book
    """
    title = models.CharField(
        max_length=70,
        help_text="The title of the book."
    )
    publication_date = models.DateField(
        verbose_name="Date the book was published."
    )
    isbn = models.CharField(
        max_length=20,
        verbose_name="ISBN number of the book."
    )
    # A book has a foreign key referring to the primary key of the Publisher table
    # this establishes a many-to-one relationship across Book and Publisher models
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )

    # A book may have multiple co-authors; Creates a many-to-many relationship with Contributor
    contributors = models.ManyToManyField(
        'Contributor',
        through="BookContributor"
    )

    def __str__(self):
        return self.title
class Contributor(models.Model):
    """Holds information about the contributor, that is, the author, co-author, editor
    - First_Names: CharField, The contributor's first name or names
    - Last_Names: CharField, the contributor's last name or names
    - Email: EmailField, The contact email for the contributor
    """
    first_names = models.CharField(
        max_length=50,
        help_text="The contributor's first name or names."
    )
    last_names = models.CharField(
        max_length=50,
        help_text="The contributor's last name or names."
    )
    email = models.EmailField(
        help_text="The contact email for the contributor"
    )

    def __str__(self):
        return self.first_names

class BookContributor(models.Model):
    """One Book can have many contributors. One contributor, can write many books. Many-to-Many relationship.
    This table serves as an intermediary table between the Book and Contributor Tables.
    - Book: Foreign Key
        - on_delete=models.CASCADE; If a book is deleted, remove its entries from this table
    - Contributor: Foreign Key
        - on_delete=models.CASCADE; If a contributor is deleted, remove its entries from this table
    - Role: CharField, The role this contributor had in the book. (Author, Co_Author, Editor)
        Choices parameter refers to a set of choices defined in the model ContributionRole, and is useful for
        creating Django Forms
    """
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    # This is a foreign key to the Book model
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    # This is a foreign key to the Contributor model
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name="The role this contributor had in the book.",
        choices=ContributionRole.choices,
        max_length=20
    )
class Review(models.Model):
    """Used to store user-provided review comments and ratings for books.
    - Content: TextField, Stores the text for a book review
    - Rating: IntegerField, The rating the reviewer has given
    - Date_created: DateTimeField, Stores the time and date when the review was written
    - Date_edited: DateTimeField, Stores the date and time whenever a review is edited
    - Creator: Foreign key; Specifies the review creator or the person who writes the book review
        - on_delete=models.CASCADE; If a user is deleted, all their reviews are deleted
    - Book: Foreign Key; The book that this review is for
        A book can have many reviews, One review is to one book, One-to-Many relationship
        - on_delete=models.CASCADE; If a book is deleted, reviews are deleted
    """

    content = models.TextField(
        help_text="The Review text."
    )
    rating = models.IntegerField(
        help_text="The rating the reviewer has given."
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the review was created."
    )
    date_edited = models.DateTimeField(
        null=True,
        help_text="The date and time the review was last edited."
    )
    creator = models.ForeignKey(
        auth.get_user_model(),
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        help_text="The Book that this review is for."
    )



