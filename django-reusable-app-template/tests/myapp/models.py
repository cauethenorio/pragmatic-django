from django.db import models

from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=30, db_column="firstname")
    last_name = models.CharField(max_length=30, db_column="last")

    class Meta:
        db_table = "my_author_table"
        ordering = ("last_name", "first_name")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    author = models.ForeignKey(Author, models.CASCADE, related_name="articles")
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    pub_datetime = models.DateTimeField(default=timezone.now)

    categories = models.ManyToManyField("Category", related_name="articles")


class Comment(models.Model):
    article = models.ForeignKey(Article, models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date = models.DateField()
    approval_date = models.DateField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=255)