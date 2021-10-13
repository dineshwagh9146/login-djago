# Generated by Django 3.2.7 on 2021-10-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=100)),
                ('Qty', models.IntegerField()),
            ],
            options={
                'db_table': 'Prod',
            },
        ),
        migrations.CreateModel(
            name='Regester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('password1', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Regester',
            },
        ),
    ]
