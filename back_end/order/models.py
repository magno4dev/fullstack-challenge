from django.db import models

# Create your models here.
class Category(models.Model):

    # tables fields
    description = models.CharField(max_length=150)
    
    # auto created date
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Pedido(models.Model):
    
    # tables fields
    contact_name = models.CharField(max_length=200)
    contact_tel = models.CharField(max_length=15)
    order_description = models.TextField()
    real_state_agency = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    dead_line = models.DateField(null=False)

    # relation with category table
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True)

    # auto created date
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name + '|' + self.contact_tel

    class Meta:
        ordering = ['created_on']

