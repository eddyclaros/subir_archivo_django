from django.db import models

class ArchivoClausula(models.Model):
    title=models.CharField(max_length=150, null=True, verbose_name="Nombre")
    file=models.FileField(upload_to='clausulas/')


    
