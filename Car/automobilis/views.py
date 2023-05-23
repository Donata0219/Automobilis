from django.shortcuts import render
from automobilis.models import Automobilis
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from pip._internal.models import index




# Create your views here.
def hello_view (reguest):
    # all_automobiliai = Automobilis.objects.all ()
    # #grazina lista    all_authors = Author.objects.filter(first_name__startswith ="S") #iesko kaip %S
    # automobilis = all_automobiliai[0]
    return HttpResponse ('Labas mielas kliente')
    # return render (reguest, index.html,{
    #     'pasisveikinimas':'Hello world!',
    #     'author':author    })