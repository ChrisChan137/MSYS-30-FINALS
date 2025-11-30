from django.db import models

class Customer(models.Model):
    # da customer id
    customer_id = models.PositiveIntegerField(unique=True)
    # da stuff for each customer
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    customer_type = models.CharField(max_length=50, blank=True)   # e.g. "VIP", "New", "Regular"
    satisfaction = models.IntegerField(default=0)  # e.g. 1–5 rating

    def __str__(self):
        return f"{self.customer_id} - {self.name}"


class Account(models.Model):
    user_name = models.CharField(unique=True, max_length=50)
    pass_word = models.CharField(max_length=50)  # (later you can switch to hashed passwords)

    # Link each account to a customer (optional but very useful in a CRM)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user_name