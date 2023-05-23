
from django.urls import path
from automobilis.views import hello_view

urlpatterns = [
    path ('hello/', hello_view)


]

