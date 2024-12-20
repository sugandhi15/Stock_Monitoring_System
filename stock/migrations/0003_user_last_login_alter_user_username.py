# Generated by Django 5.1.3 on 2024-11-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_user_remove_stock_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
