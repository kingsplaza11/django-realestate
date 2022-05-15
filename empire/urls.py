from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('contacts', views.contacts, name = "contacts" ),
    path('success', views.success, name="success"),
    path('order-in-proccess', views.order_in_p, name="order-in-proccess" ),
    path('ceeus/', views.ceeus, name="ceeus"),
    path('listing/<slug>', PropertyDetailView.as_view(), name='listing'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('about/', AboutView.as_view(), name='about'),
]