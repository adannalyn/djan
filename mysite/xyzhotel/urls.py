from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('book_now',views.book_now,name='book_now'),
    path('contact-us',views.contact,name='contact-us'),
]
