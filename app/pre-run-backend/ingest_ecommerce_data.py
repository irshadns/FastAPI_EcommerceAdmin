from datetime import datetime, timedelta
from random import randint, uniform

from faker import Faker

from app.database import SessionLocal
from app.ecommerce.models import Product, Sale, Inventory

# Create Faker instance
fake = Faker()


# Function to generate a random datetime within the last 30 days
def random_past_date():
    days = randint(1, 30)
    return datetime.now() - timedelta(days=days)


# Function to create a random product
def create_random_product():
    # Generate a random product name
    product_name = f'{fake.company()} {fake.word()}'

    # Generate a product description with multiple sentences
    product_description = fake.paragraph(nb_sentences=3)

    # Generate a random price between $1 and $100
    product_price = round(uniform(1.0, 100.0), 2)

    # Generate a random date for product creation within the last 30 days
    product_created_at = random_past_date()

    return Product(
        name=product_name,
        description=product_description,
        price=product_price,
        created_at=product_created_at,
    )


# Function to create a random sale record
def create_random_sale(product):
    return Sale(
        product=product,
        quantity=randint(1, 10),
        total_price=round(uniform(10.0, 500.0), 2),
        sale_date=random_past_date(),
    )


# Function to create a random inventory record
def create_random_inventory(product):
    return Inventory(
        product=product,
        quantity=randint(10, 100),
        last_updated=random_past_date(),
    )


# Create 100 dummy records for each model
with SessionLocal() as session:
    for _ in range(100):
        product = create_random_product()
        session.add(product)
        session.commit()

        sale = create_random_sale(product)
        session.add(sale)

        inventory = create_random_inventory(product)
        session.add(inventory)

        session.commit()
