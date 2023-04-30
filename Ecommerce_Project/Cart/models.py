from django.db import models
from Shop.models import Product
# Create your models here.
class Cart(models.Model):
    Cart_id=models.CharField(max_length=250,blank=True)
    Date_Added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['Date_Added']

    def __str__(self):
        return '{}'.format(self.Cart_id)

class CartItem(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItem'

    def Sub_Total(self):
        return self.Product.Price * self.Quantity
    def __str__(self):
        return '{}'.format(self.Product)


