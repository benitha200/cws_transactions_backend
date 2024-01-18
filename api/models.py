from django.db import models


class UserRole(models.Model):
    role=models.TextField(max_length=255)
    def __str__(self) -> str:
        return self.role

        
