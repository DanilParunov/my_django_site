# Generated by Django 3.1.2 on 2020-12-02 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20201123_1157'),
        ('accounts', '0005_auto_20201202_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='books',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='list.articles'),
            preserve_default=False,
        ),
    ]
