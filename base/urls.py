from django.urls import path
from . import views
from .views import AddItem


urlpatterns = [
    path('', views.index, name='home'),
    path('items/', views.items_page, name='items'),
    path('add_items/', AddItem.as_view(), name='add_item'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
