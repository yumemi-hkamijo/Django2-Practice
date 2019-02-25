from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = 'book'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    image = models.ImageField(verbose_name='画像', null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, verbose='出版社', on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author, verbose_name='著者')
    description = models.TextField(verbose_name='概要', null=True, blank=True)
    publish_date = models.DateField(verbose_name='出版日')

    def __str__(self):
        return self.title

class BookStock(models.Model):
    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)

class Publisher(models.Model):
    class Meta:
        db_table = 'publisher'

    name = models.CharField(verbose_name='出版社名', max_length=255)

    def __str__(self):
        return self.name

class Author(models.Model):
    class Meta:
        db_table = 'author'

    name = models.CharField(verbose_name='著者名', max_length=255)

    def __str__(self):
        return self.name