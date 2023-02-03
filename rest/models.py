from django.db import models
from django.contrib.postgres.fields import ArrayField




class Notes(models.Model):
    title = models.CharField(max_length=30)

class IdentifiedErrors(models.Model):
    error_id = models.CharField(max_length=10)
    error_desc = models.CharField(max_length=30)
    error_type = models.CharField(max_length=10)

class OnNotice(models.Model):
    analyst_name = models.CharField(max_length=50)
    days_onnotice = ArrayField(
        ArrayField(
            models.IntegerField(blank=True),
            size=8
        ),
        size=8
    )

class Flows(models.Model):
    automatic_flow = ArrayField(
        ArrayField(
            models.IntegerField(blank=True),
            size=8
        ),
        size=8
    )

    manual_flow = ArrayField(
        ArrayField(
            models.IntegerField(blank=True),
            size=8
        ),
        size=8
    )

    semi_auto_flow = ArrayField(
        ArrayField(
            models.IntegerField(blank=True),
            size=8
        ),
        size=8
    )

class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    siem_name = models.CharField(max_length=30)
    status = models.CharField(max_length=10)

class Caser(models.Model):
    case_number = models.CharField(max_length=10)
    short_description = models.CharField(max_length=50)
    case_date = models.DateField()


class TicketsList(models.Model):
    id = models.CharField(max_length=14, primary_key=True)
    description = models.CharField(max_length=100)
    customer = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    priority = models.CharField(max_length=6)
    status = models.CharField(max_length=10)
    create_date = models.DateTimeField()

