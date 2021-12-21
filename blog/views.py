from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def index(request):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood")
    jsonResponse = response.json()
    meals = jsonResponse['meals']
    return render(request, 'blog/index.html', {'meals':meals})

def specific(request):
    return HttpResponse("This is my specific url")

def article(request, article_id):
    return render(request, 'blog/index.html',{'article_id':article_id})

def singleMeal(request):
    mealID = request.GET.get('mealID')
    response = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i="+str(mealID))
    jsonREsponse = response.json()
    meals = jsonREsponse['meals']
    return render(request, 'blog/singleMeal.html', {'meals':meals})

def about(request):
    return render(request, 'blog/about.html')
def contact(request):
    return render(request, 'blog/contact.html')