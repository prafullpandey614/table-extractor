from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="uploads")
    extracted_table_txt = models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.id} {self.file} "
    

    