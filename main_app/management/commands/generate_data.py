import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
from faker import Faker
import numpy as np  # Optional for performance, can use random.choices otherwise

from main_app.models import FredUser, Order, OrderItem, Product

class Command(BaseCommand):
    help = 'Generates large test datasets'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=20000, help='Number of users to create')
        parser.add_argument('--products', type=int, default=1000, help='Number of products to create')
        parser.add_argument('--orders', type=int, default=100000, help='Number of orders to create')
        parser.add_argument('--orderitems', type=int, default=300000, help='Number of order items to create')

    def handle(self, *args, **options):
        fake = Faker()
        Faker.seed(0)  # For consistent results

        self.generate_users(fake, options['users'])
        self.generate_products(fake, options['products'])
        self.generate_orders(fake, options['orders'])
        self.generate_order_items(fake, options['orderitems'])

    @transaction.atomic
    def generate_users(self, fake, num_users):
        self.stdout.write(f"Creating {num_users} users...")
        batch_size = 1000
        users = []
        used_usernames = set()

        while len(users) < num_users:
            username = fake.numerify('9#########')  # 10-digit phone number
            if username not in used_usernames:
                used_usernames.add(username)
                user = FredUser(
                    username=username,
                    modified_date=fake.date_time_between(start_date='-2y', end_date='now'),
                    date_joined=fake.date_time_between(start_date='-2y', end_date='now'),
                )
                user.set_password('password')
                users.append(user)
                if len(users) % batch_size == 0:
                    FredUser.objects.bulk_create(users, batch_size)
                    users = []
        if users:
            FredUser.objects.bulk_create(users, batch_size)

    @transaction.atomic
    def generate_products(self, fake, num_products):
        self.stdout.write(f"Creating {num_products} products...")
        batch_size = 500
        products = []

        for _ in range(num_products):
            created_date = fake.date_time_between(start_date='-2y', end_date='now')
            products.append(Product(
                name=fake.text(max_nb_chars=50),
                price=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
                created_date=created_date,
                modified_date=fake.date_time_between(start_date=created_date, end_date='now'),
            ))
            if len(products) % batch_size == 0:
                Product.objects.bulk_create(products, batch_size)
                products = []
        if products:
            Product.objects.bulk_create(products, batch_size)

    @transaction.atomic
    def generate_orders(self, fake, num_orders):
        self.stdout.write(f"Creating {num_orders} orders...")
        batch_size = 5000
        user_ids = list(FredUser.objects.values_list('id', flat=True))
        orders = []

        # Generate random dates and user assignments
        for _ in range(num_orders):
            created_date = fake.date_time_between(start_date='-1y', end_date='now')
            orders.append(Order(
                user_id=random.choice(user_ids),
                created_date=created_date,
                modified_date=fake.date_time_between(start_date=created_date, end_date='now'),
            ))
            if len(orders) % batch_size == 0:
                Order.objects.bulk_create(orders, batch_size)
                orders = []
        if orders:
            Order.objects.bulk_create(orders, batch_size)

    @transaction.atomic
    def generate_order_items(self, fake, num_order_items):
        self.stdout.write(f"Creating {num_order_items} order items...")
        batch_size = 10000
        order_ids = list(Order.objects.values_list('id', flat=True))
        product_ids = list(Product.objects.values_list('id', flat=True))
        order_items = []

        # Use numpy for faster random sampling (or random.choices)
        order_indices = np.random.choice(len(order_ids), num_order_items)
        product_indices = np.random.choice(len(product_ids), num_order_items)

        for i in range(num_order_items):
            created_date = fake.date_time_between(start_date='-6m', end_date='now')
            order_items.append(OrderItem(
                order_id=order_ids[order_indices[i]],
                product_id=product_ids[product_indices[i]],
                quantity=random.randint(1, 10),
                created_date=created_date,
                modified_date=fake.date_time_between(start_date=created_date, end_date='now'),
            ))
            if len(order_items) % batch_size == 0:
                OrderItem.objects.bulk_create(order_items, batch_size)
                order_items = []
        if order_items:
            OrderItem.objects.bulk_create(order_items, batch_size)



