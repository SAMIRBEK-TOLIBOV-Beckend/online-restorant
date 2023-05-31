from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# from django.core.validators import MinLengthValidator



# Create your models here.


class Login(models.Model):
    f_name = models.CharField(max_length=255, null=True, blank=True)
    l_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    password = models.IntegerField(max_length=150, null=True, blank=True)
    confirm_password = models.IntegerField(max_length=150, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.username
    
class Food(models.Model):
    food_name = models.CharField(max_length=250, null=True, blank=True)
    food_price = models.IntegerField(max_length=200, null=True, blank=True)
    food_ingredient = models.TextField(null=True, blank=True)
    food_image = models.ImageField(upload_to="fast-food", null=True, blank=True)
    prep_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.food_name
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    table = models.CharField(max_length=120, null=True, blank=True)
    food = models.ManyToManyField(Food, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user
    
    def __str__(self):
        return str(self.id)
    
    
    
class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    

