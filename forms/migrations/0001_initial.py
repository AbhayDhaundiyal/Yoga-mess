# Generated by Django 4.1.4 on 2022-12-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.TextField()),
                ('DOB', models.DateField()),
                ('Payment_Date', models.DateField()),
            ],
        ),
    ]