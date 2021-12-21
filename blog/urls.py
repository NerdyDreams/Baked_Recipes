from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('specifics',views.specific, name='specifics'),
    path('article/<int:article_id>', views.article, name='article'),
    path('singleMeal', views.singleMeal, name ='singleMeal'),
    path('about', views.about, name ='about'),
    path('contact', views.contact, name ='contact')
]