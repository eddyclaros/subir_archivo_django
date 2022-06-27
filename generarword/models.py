from django.db import models

class Clausulas(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, null=True, verbose_name="Título")
    subtitle=models.CharField(max_length=100,null=True, verbose_name="Subtitulo")
    numpoliza=models.CharField(max_length=50,null=True, verbose_name="Numero poliza")
    nameaseg=models.CharField(max_length=50,null=True, verbose_name="Asegurado" )
    textpoliza=models.TextField(verbose_name="Parrafos")

