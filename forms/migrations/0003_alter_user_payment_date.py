# Generated by Django 4.1.4 on 2022-12-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_user_batch_alter_user_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Payment_Date',
            field=models.DateField(default=998),
        ),
    ]