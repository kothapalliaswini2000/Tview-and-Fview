# Generated by Django 5.0.3 on 2024-06-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cprincipal', models.CharField(max_length=100)),
                ('cloc', models.CharField(max_length=100)),
            ],
        ),
    ]
