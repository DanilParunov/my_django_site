# Generated by Django 3.1.2 on 2020-12-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20201123_1157'),
        ('accounts', '0009_auto_20201202_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='books',
            field=models.ManyToManyField(to='list.Articles'),
        ),
    ]
