from django.db import models

class Publisher(models.Model):
    """
    A company that publishes books that contains:
        - name
        - website
        - email
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

class Book(models.Model):
    """
    A published book that contains:
        - title
        - isbn
        - publisher
    """
    title = models.CharField(
        max_length=70,
        help_text="The title of the book."
    )
    isbn = models.CharField(
        max_length=20,
        verbose_name="ISBN number of the book."
    )
    # A book has a foreign key referring to the primary key of the Publisher table
    # this establishes a many-to-one relationship across Book and Publisher models
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE
    )

    ## A book may have multiple co-authors; Creates a many-to-many relationship with Contributor
    contributors = models.ManyToManyField(
        'Contributor',
        through="BookContributor"
    )
class Contributor(models.Model):
    """
    A contributor to a Book, e.g. author, editor, co-author:
        - first name
        - last name
        - email
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

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR - "EDITOR", "Editor"
    # This is a foreign key to the Book model
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE
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





