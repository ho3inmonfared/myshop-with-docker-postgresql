from django.db import models
from django.urls import reverse

class Product(models.Model):
    
    STATUS_CHOICES = (
        (True,'موجود', ),
        (False,'ناموجود', )
    )
    
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=0)
    status=models.BooleanField(default=True, choices=STATUS_CHOICES)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
