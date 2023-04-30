from django.urls import path
from . import views

app_name='Cart'

urlpatterns=[
    path('add/<int:Product_id>/',views.Add_Cart,name='Add_Cart'),
    path('',views.Cart_Detail,name='Cart_Detail'),
    path('remove/<int:Product_id>/',views.Cart_Remove,name='Cart_Remove'),
    path('Full_Remove/<int:Product_id>/', views.Full_Remove, name='Full_Remove'),
]