from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)

