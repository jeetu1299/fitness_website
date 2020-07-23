from django.shortcuts import render,redirect,render_to_response
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None : 
            auth.login(request,user)
            Profiles = Profile.objects.all()
            print(user.pk)
            for p in Profiles :
                print(p.user_id)
                if(user.pk==p.user_id):
                    position = p.position
            if(position == "customer"):
                return redirect('/')
            if(position == "trainer"):
                return redirect('/')
        else :
            return redirect('/')
    else:
        return render(request,'login.html')

def pricing(request):
    return render(request,'pricing.html')
def trainers(request):
    trainers = Trainer.objects.all()
    return render(request,'trainers.html',{'trainers':trainers})
def signup(request):
    if request.method == 'POST' : 
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=name).exists():
            return render_to_response('message.html', {'message':'Username Taken'})
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            return render_to_response('message.html', {'message':'Email Id Taken'})
            return redirect('/')
        else :
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
        position = 'customer'
        cats = Meals.objects.all()
        category = request.POST.get('category')
        print(category)
        for cat in cats:
            if(cat.name == category):
                mealId = cat
        profile = Profile.objects.create(user=user,position=position,mealId=mealId)
        profile.save()

        plan = request.POST.get('plan') 
        trainers = Trainer.objects.all()
        for trainer in trainers :
            if(trainer.mealId.name==category):
                train = trainer
        customer = Customer.objects.create(name=name,pricing=plan,trainerId=train)
        print("User created")
        return redirect('pay')
    else:
        plan = Meals.objects.all()
        return render(request,'signup.html',{'plan':plan})

def recepies(request):  
    customer = Customer.objects.all()
    meals = Meals.objects.all()
    profile = Profile.objects.all()
    current_user = request.user
    data = 0
    for p in profile:
        if(current_user.pk == p.user_id):
            data = p.mealId
    return render(request,'recepies.html',{'meals':meals,'data':data})

def pay(request):
    if(request.method=="POST"):
        return render_to_response('message.html', {'message':'Payment successfull'})
    else:    
        plans = Meals.objects.all()
        return render(request,'pay.html',{'plans':plans})

def logout(request):
    auth.logout(request)
    return redirect('/')

def workout(request):
    return render(request,'workout.html')

def about(request):
    return render(request,'about.html')

def user(request):
    profile = Profile.objects.all()
    current_user = request.user
    u = current_user
    trainers = Trainer.objects.all()
    for profile in profile:
        if profile.user_id == current_user.pk:
            p = profile.mealId
    for trainer in trainers : 
        if trainer.mealId==p:
            t = trainer
    customers = Customer.objects.all()

    for customer in customers :
        if customer.trainerId==t :
            c = customer

    return render(request,'user.html',{'profile':p,'trainer':t,'customer':c})

def contact(request):
    return render(request,'contact.html')
def message(request):
    return render(request,'message.html')