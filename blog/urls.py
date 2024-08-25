from django.urls import path
# from django.views.decorators.cache import cache_page

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('post/<str:slug>/', views.GetPost.as_view(), name='single_post'),
]


