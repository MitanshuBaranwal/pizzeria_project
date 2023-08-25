from celery import shared_task
from django.utils import timezone
from .models import Order, OrderStatus
import time
from django.core.exceptions import ObjectDoesNotExist

@shared_task
def update_order_status(order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except ObjectDoesNotExist:
        print(f"Order with id {order_id} does not exist.")
        return

    while True:
        current_time = timezone.now()
        elapsed_time = (current_time - order.created_at).total_seconds()
        print(elapsed_time)
        if elapsed_time < 120:
             OrderStatus.objects.create(order=order, status='Accepted')
        elif elapsed_time >= 120 and elapsed_time < 240:
            OrderStatus.objects.create(order=order, status='Preparing')
        elif elapsed_time >= 240 and elapsed_time < 360:
            OrderStatus.objects.create(order=order, status='Dispatched')
        elif elapsed_time > 360:
            OrderStatus.objects.create(order=order, status='Delivered')
            break

        # Sleep for a while before checking again (e.g., every minute)
        time.sleep(60)  # Sleep for 60 seconds (1 minute) before checking again
