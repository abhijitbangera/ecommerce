from django.db import models
from django.conf import settings
from products.models import Variation
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from decimal import Decimal


class CartItem(models.Model):
	cart=models.ForeignKey("Cart")
	item=models.ForeignKey(Variation)
	quantity=models.PositiveIntegerField(default=1)
	line_item_total=models.DecimalField(max_digits=10,decimal_places=2)
	# line_total=models.DecimalField(max_digits=10,decimal_places=2)
	def __str__(self):
		return self.item.title
	def remove(self):
		return self.item.remove_from_cart()
	def get_title(self):
		return "%s - %s" %(self.item.product.title, self.item.title)

def cart_item_pre_save_receiver(sender,instance,*args,**kwargs):
	qty=instance.quantity
	if int(qty) >=1:
		price=instance.item.get_price()
		line_item_total=Decimal(qty)*Decimal(price)
		instance.line_item_total=line_item_total
pre_save.connect(cart_item_pre_save_receiver,sender=CartItem)



def cart_item_post_save_receiver(sender,instance,*args,**kwargs):
	instance.cart.update_subtotal()
post_save.connect(cart_item_post_save_receiver,sender=CartItem)

# Create your models here.
class Cart(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
	items=models.ManyToManyField(Variation,through=CartItem)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	subtotal=models.DecimalField(max_digits=50,decimal_places=2)
	def __str__(self):
		return str(self.id)

	def update_subtotal(self):
		subtotal=0
		items=self.cartitem_set.all()
		for item in items:
			subtotal+=item.line_item_total
		self.subtotal=subtotal
		self.save() 