# Generated by Django 3.2.8 on 2022-06-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoClausula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
