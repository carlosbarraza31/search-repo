from django.forms.fields import CharField
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):
    allWords = forms.CharField(label = "all these words", help_text="Type important words. ")
    exactWords = forms.CharField(label = "this exact word or phrase", help_text = "Type exact words between quotes. ")
    anyWords = forms.CharField(label = "any of these words", help_text = "Type 'OR' between words. ")
    noneWords = forms.CharField(label = "none of these words", help_text = "Type a minus sign right after words you do not wish to appear. ")
    numbersFrom = forms.CharField(label = "numbers from")
    numbersTo = forms.CharField(label = "to")

pages = [
            [{"name": 'Atlas Search', "url": "{% url 'homepage/' %}"}],
            [{"name": 'Image Search', "url": "{% url 'homepage/imageSearch' %}"}],
            [{"name": 'Advanced Search', "url": "{% url 'homepage/advancedSearch' %}"}]
        ]
indexPages = pages[1] + pages[2]
imagePages = pages[0] + pages[2]
advancedPages = pages[0] + pages[1]

def index(request):
    return render(request, "homepage/index.html")

def imageSearch(request):
    return render(request, "homepage/imageSearch.html", {
        "pages": pages[0] + pages[2]
    })  
def advancedSearch(request):
    return render(request, "homepage/advancedSearch.html", {
        "pages": pages[0] + pages[1],
        "form": NewTaskForm()
    })

