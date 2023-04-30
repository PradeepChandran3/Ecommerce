from django.urls import path
from.import views

app_name="Shop"
urlpatterns = [
    path('',views.AllProductCategory,name='AllProductCategory'),
    path('<slug:C_Slug>/',views.AllProductCategory,name='Products_By_Category'),
    path('<slug:C_Slug>/<slug:Product_Slug>/',views.ProductDetail,name='Products_Category_Detail'),
]