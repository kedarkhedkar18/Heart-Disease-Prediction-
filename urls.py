


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home Page
    path('predict/', views.predict, name='predict'),  # Prediction Form Page
     path('about/', views.about, name='about'),  # About Page
]
