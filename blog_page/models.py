from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["-category_name"]

    def __str__(self):
        return self.category_name


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=64)
    author_mail = models.EmailField()

    class Meta:
        verbose_name_plural = "Authors"
        ordering = ["-author_name"]

    def __str__(self):
        return self.author_name


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_category = models.ForeignKey(Category)
    post_title = models.CharField(max_length=256)
    post_content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ["-post_date"]

    def __str__(self):
        return self.post_title
