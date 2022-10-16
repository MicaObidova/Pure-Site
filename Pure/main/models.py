from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class SubCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    subcat = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.name

class Information(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='product_image')
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    bonus = models.DecimalField(decimal_places=2,max_digits=50)
    rating = models.IntegerField(default=0)
    info = models.ManyToManyField(Information)
    description = models.TextField(blank=True)
    availability = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}| {self.category.name}'

class Author(models.Model):
    image = models.ImageField(upload_to='author_image', blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name






class Blog(models.Model):
    name = models.CharField(max_length=255, default='Fusce blandit nulla at massa venenatis, sed tincidunt nisltincidunt.')
    image = models.ImageField(upload_to='blog_image')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300, blank=True)
    avtor = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f' Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def sumbonus(self):
        return self.quantity * self.product.bonus

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=250)
    index = models.IntegerField(default=170100)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()

class Expert(models.Model):
    image = models.ImageField(upload_to='team_image')
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    image = models.ImageField(upload_to='review_image')
    name = models.CharField(max_length=250)
    description = models.TextField()

class Comment(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    image = models.ImageField(upload_to='comment_image')
    date = models.DateTimeField(auto_now_add=True)