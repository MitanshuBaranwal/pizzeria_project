# Pizza Ordering System

This is a pizza ordering system built using Django and Django Rest Framework and hosted on Docker. It allows users to place pizza orders, calculate the price based on their choice of pizza, and track the status of their orders.

## Features

- **Pizza Price Calculation**: The system calculates the price of the pizza based on the selected base, cheese, and toppings.

- **Order Placement**: Users can place pizza orders, and the system will generate an order ID for each order.

- **Order Tracking**: Users can track the status of their orders, including whether it's placed, accepted, preparing, dispatched, or delivered.

## Getting Started

### Prerequisites

- Python (3.7+)
- Django (3.2+)
- Django Rest Framework (3.12+)
- Celery (5.0+)
- Docker (24.0+)
### Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/MitanshuBaranwal/pizzeria_project.git
   ```


2. Change directory to the project folder:
    ```
    cd pizzeria_project
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Apply the database migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Start the Celery worker to handle order status updates in the background:
    ```
    celery -A pizzeria_project worker --pool=solo -l info
    ```
6. Start the Django development server:
    ```
    python manage.py runserver
    ```

Usage
Calculate Pizza Price
To calculate the price of a pizza, make a POST request to the /api/get-price/ endpoint with the desired pizza configuration, including the base, cheese, and toppings in the request body.

Example request body:
  http://127.0.0.1:8000/api/get-price/

    
      {
          "base": "cheese-burst",
          "cheese": "gouda",
          "toppings": ["Pepperoni","Mushrooms","Onions","Green Peppers","Olives"]
      }
    
    
Place an Order
  To place a pizza order, make a POST request to the /api/create-order/ endpoint with the desired pizza configuration, including the base, cheese, and toppings in the request body.

Example request body:
  http://127.0.0.1:8000/api/create-order/

    
      {
          "base": "cheese-burst",
          "cheese": "gouda",
          "toppings": ["Pepperoni","Mushrooms","Onions","Green Peppers","Olives"]
      }
      
    
Track an Order
     To track the status of an order, make a GET request to the /api/track_order/{order_id}/ endpoint, where {order_id} is the order's ID you want to track.

Example request:
     http://127.0.0.1:8000/api/track-order/1/

