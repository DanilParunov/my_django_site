# Generated by Django 3.1.2 on 2020-12-02 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customers_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='books',
        ),
    ]