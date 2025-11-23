import random

def generate_unique_seller_id() -> int:
    return random.randint(1000000, 9999999)

def generate_name() -> str:
    brands = ["iPhone", "Samsung", "Xiaomi", "MacBook", "PlayStation", "Nike", "BMW", "Toyota", "Sony", "Canon"]
    models = ["15 Pro", "S24 Ultra", "14T Pro", "Air M2", "5", "Air Force 1", "X5", "Camry", "A7", "EOS R5"]
    condition = ["новый", "б/у", "в идеале", "срочно", "торг", "2024 года", ""]
    return f"{random.choice(brands)} {random.choice(models)} {random.choice(condition)}".strip()