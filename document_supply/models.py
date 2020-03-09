from django.db import models

# Create your models here.

class Apply_user(models.Model) :
    name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    grade = models.IntegerField(blank=True)
    grade_num = models.CharField(max_length=20, blank=True)
    motivation = models.TextField(blank=True)
    webservice = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    getting = models.TextField(blank=True)

    def __str__ (self) :
        return self.name