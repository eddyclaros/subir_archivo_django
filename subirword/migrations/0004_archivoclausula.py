# Generated by Django 3.2.8 on 2022-06-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subirword', '0003_delete_archivoclausula'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoClausula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True, verbose_name='Nombre')),
                ('file', models.FileField(upload_to='clausulas/%Y/%m/%d')),
            ],
        ),
    ]
