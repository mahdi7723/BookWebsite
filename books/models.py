from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='books/', default='books/default.jpeg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Add any additional fields as per your requirements

    def __str__(self):
        return self.title
