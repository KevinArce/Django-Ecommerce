from django.urls import path # import path function from django.urls module to use it in the urls.py file to define the URL patterns
from . import views # import views module from the same directory as urls.py file

# URLConf for the playground app (playground) (urls.py)
urlpatterns = [ # define the URL patterns for the playground app 
    path('hello/', views.say_hello), 
] # end of the URL patterns for the playground app
