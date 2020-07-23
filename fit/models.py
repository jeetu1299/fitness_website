from django.db import models

class Meals(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField(max_length = 500)
    image = models.ImageField(upload_to='meals')
    file = models.FileField(upload_to='pdf')

class Trainer(models.Model):
    name = models.CharField(max_length=70)
    salary = models.IntegerField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='trainers')
    desc = models.TextField(max_length=200)
    mealId = models.ForeignKey(Meals, on_delete = models.PROTECT)

class Profile(models.Model):
    customer = 'customer'
    trainer = 'trainer'
    POSITION_CHOICES = (
        (customer, 'customer'),
        (trainer, 'trainer'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    position = models.CharField(
    max_length=20,
    choices=POSITION_CHOICES, default = customer
    )
    mealId = models.ForeignKey(Meals, on_delete = models.PROTECT)

class Customer(models.Model):
    name = models.CharField(max_length=70)
    basic='basic'
    pro='pro'
    premium='premium'
    PRICING = (
        (basic,'basic'),
        (pro,'pro'),
        (premium,'premium'), 
    )
    pricing = models.CharField(
    max_length=20,
    choices=PRICING, default = basic
    )
    trainerId = models.ForeignKey(Trainer, on_delete = models.PROTECT)

