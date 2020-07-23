from django.contrib import admin
from .models import * 

myModels = [Meals,Trainer,Profile,Customer]  # iterable list
admin.site.register(myModels)