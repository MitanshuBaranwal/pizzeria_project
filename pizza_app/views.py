from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderStatus
from .serializers import OrderSerializer, OrderStatusSerializer
from .tasks import update_order_status

# Define pizza prices in a dictionary
PRICES_DICT = {
    "thin-crust": 100,
    "normal": 120,
    "cheese-burst": 130,
    'mozarella': 25,
    'cheddar': 20,
    'parmesan': 25,
    'gouda': 30,
    'Pepperoni': 10,
    'Mushrooms': 15,
    'Onions': 5,
    'Green Peppers': 8,
    'Olives': 7,
}

def calculate_price(request):
    base = request.data.get('base', '')
    cheese = request.data.get('cheese', '')
    toppings = request.data.get('toppings', [])
    toppings_price = sum(PRICES_DICT.get(topping, 0) for topping in toppings)
    price = PRICES_DICT.get(base, 0) + PRICES_DICT.get(cheese, 0) + toppings_price

    return price

@api_view(['POST'])
def get_price(request):
    try:
        price = calculate_price(request)
        response_data = {
            "price": price,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_order(request):
    price = calculate_price(request)
    request.data['price'] = price

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        order = serializer.save()
        OrderStatus.objects.create(order=order, status='Placed')
        update_order_status.apply_async((order.id,), countdown=60)
        response_data = {
            "message": "Order placed successfully.",
            "order_id": order.id,
            "price": order.price,
            "status": "Placed"
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def track_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    order_status = OrderStatus.objects.filter(order=order).order_by('-timestamp').first()

    if not order_status:
        return Response({'status': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderStatusSerializer(order_status)
    return Response(serializer.data)
