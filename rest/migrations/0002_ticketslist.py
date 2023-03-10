# Generated by Django 4.1.5 on 2023-02-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketsList',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=6)),
                ('status', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
