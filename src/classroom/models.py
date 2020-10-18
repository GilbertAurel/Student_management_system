from django.db import models

# Create your models here.


class Classroom(models.Model):
    class_id = models.CharField(max_length=10, blank=False, null=False) # missing  PK
    student_id = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return "Class_ID : {0}, Student_ID: {1}".format(self.class_id, self.student_id)