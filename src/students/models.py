from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.CharField(max_length=10, blank=False, null=False) # missing  PK
    student_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return "ID : {0}, name: {1}".format(self.student_id, self.student_name)