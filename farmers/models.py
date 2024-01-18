from django.db import models


class Farmer(models.Model):
    cws = models.TextField(max_length=255,default=None)
    farmer_code = models.TextField(max_length=255, unique=True)
    farmer_name = models.TextField(max_length=255)
    gender = models.TextField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(max_length=255)
    phone_number = models.TextField(max_length=20)
    national_id = models.TextField(max_length=20,unique=True,default=0)
    village = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Allow null for created_at
    created_by = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.farmer_name} - {self.farmer_code}"

    class Meta:
        db_table='farmer_details'