from django.urls import path, include
from django.views.generic import ListView, DetailView
from price.models import Price


urlpatterns = [
    path('', 
    ListView.as_view(queryset=Price.objects.all().order_by('-date')[:20], 
    template_name='price/posts.html')), 
    path('<pk>', DetailView.as_view(model= Price, template_name= 'price/post.html'))
    
]
