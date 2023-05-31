from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Login)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Comment)

