from django.shortcuts import render,redirect
from .models import GuestProfile
from .models import Rooms,Booking
from django.contrib import messages
from django.http import HttpResponse
import datetime
def index(request):
    return render(request,'xyzhotel/booking/index.html',{})
def contact(request):
    if request.method=="GET":
     return render(request,"xyzhotel/contact/contact.html",{})
    else:
     username=request.POST['name']
     occupation=request.POST['message']
     email=request.POST['email']
     data=Contact(name=username,message=message,email=email)
     data.save()
     return render(request,"xyzhotel/contact/contact.html",{'message':'Thank you for contacting us.'})
def book(request):
    if request.method=="POST":
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        request.session['start_date']=start_date
        request.session['end_date']=end_date
        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
        no_of_nights=(end_date-start_date).days
        data=Rooms.objects.filter(is_available=True)
        request.session['no_of_nights']=no_of_nights
        return render(request,'xyzhotelbooking/book.html',{'data':data})
    else:
        return redirect('index')
def book_now(request,id):
    if request.session.get("username",None) and request.session.get("type",None)=='customer':
        if request.session.get("no_of_nights",1):
            no_of_nights=request.session['no_of_nights']
            start_date=request.session['start_date']
            end_date=request.session['end_date']
            request.session['room_no']=id
            data=Rooms.objects.get(room_no=id)
            bill=data.price*int(no_of_nights)
            request.session['bill']=bill
            roomManager=data.manager.username
            return render(request,"booking/book-now.html",{"no_of_nights":no_of_nights,"room_no":id,"data":data,"bill":bill,"roomManager":roomManager,"start":start_date,"end":end_date})
        else:
            return redirect("index")
    else:
        next="book-now/"+id
        return redirect('user_login')