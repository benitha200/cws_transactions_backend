from django.db import models

class Cws(models.Model):
    cws_code = models.TextField(max_length=255, default=None)
    cws_name = models.TextField(max_length=20,default=None)

    def __str__(self) -> str:
        return self.cws_name
    class Meta:
        db_table='cws'