from django.db import models


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_fname = models.CharField(max_length=50)
    emp_lname = models.CharField(max_length=50)
    emp_email = models.CharField(max_length=80)
    emp_phone = models.CharField(max_length=20)
    emp_address = models.TextField()
    emp_status = models.CharField(max_length=8)
    emp_created_on = models.DateTimeField()
    emp_updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee'


class ProductsOffer(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10)
    descriptions = models.CharField(max_length=300)
    discount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'products_offer'


class ProductsProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)

    class Meta:
        managed = False
        db_table = 'products_products'