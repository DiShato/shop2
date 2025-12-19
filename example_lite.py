import products 
from user import Customer, Admin
from shopingcart import ShoppingCart


# Создаем продукты
laptop = products.Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = products.Clothing(name="Футболка", price=200, size="M", material="Хлопок")
soap = products.Chemicals(name="Мыло", price=70, description = 'Мыло хозяйственное')

# Создаем пользователей
customer = Customer(username="Ali", email="python@gmail.ru", password='vgbhjnomkp,l', address="042 Russ Kem")
admin = Admin(username="root", email="root@gmail.ru", password='dfygyuhjioklkijuhgvfcdxc', admin_level=5)

# Создаем корзину покупок, добавляем товары и регистрируем покупку
cart = ShoppingCart()
cart.add_item(soap, 2)
cart.add_item(tshirt, 3)

# Выводим детали корзины
print(cart.get_details(customer, payment_receipt_status = 'success'))

