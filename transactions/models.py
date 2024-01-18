from django.db import models

class Transactions(models.Model):
    cws_name = models.TextField(max_length=255)
    purchase_date = models.DateField()
    farmer_code = models.TextField(max_length=255)
    farmer_name = models.TextField(max_length=255)
    season = models.IntegerField()
    cherry_kg = models.DecimalField(max_digits=10, decimal_places=2)
    has_card = models.IntegerField()
    cherry_grade = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    paper_grn_no = models.TextField(max_length=20)
    transport = models.DecimalField(max_digits=10, decimal_places=2) 
    batch_no = models.TextField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'

    def __str__(self) -> str:
        return f"{self.cws_name}-{self.purchase_date}--{self.farmer_name}--{self.batch_no}"
