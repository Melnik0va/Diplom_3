import random 
import string 
from faker import Faker

fake = Faker()

def generate_user_info(): 
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(5)

    user = {
        'email': f'{login}@tester.ru',
        'password': f'{fake.password()}',
        'name' : f'{fake.name()}'
    }

    return user