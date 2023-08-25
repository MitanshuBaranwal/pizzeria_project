from django.db import models

#model which stores Pizza choice of user
class Order(models.Model):
    BASE_CHOICES = [
        ('thin-crust', 'Thin Crust'),
        ('normal', 'Normal'),
        ('cheese-burst', 'Cheese Burst'),
    ]

    CHEESE_CHOICES = [
        ('mozarella', 'Mozarella'),
        ('cheddar', 'Cheddar'),
        ('parmesan', 'Parmesan'),
        ('gouda', 'Gouda'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    base = models.CharField(max_length=255, choices=BASE_CHOICES, default='normal')
    cheese = models.CharField(max_length=255, choices=CHEESE_CHOICES, default='mozarella')
    toppings = models.CharField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def set_toppings(self, toppings_list):
        # Convert the list of toppings to a comma-separated string
        self.toppings = ",".join(toppings_list)

    def get_toppings(self):
        # Split the comma-separated string into a list of toppings
        if self.toppings:
            return self.toppings.split(",")
        else:
            return []

    def __str__(self):
        return f"Order {self.id}"

#model which stores Order Status
class OrderStatus(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Placed', 'Placed'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES, default='Placed')
    timestamp = models.DateTimeField(auto_now_add=True)
