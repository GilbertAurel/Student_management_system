from django.db import models

# Create your models here.


class Class(models.Model):
    class_id = models.CharField(max_length=10, blank=False, null=False) # missing  PK
    class_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return "ID : {0}, Name: {1}".format(self.class_id, self.class_name)