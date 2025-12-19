# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total
    
    # def get_details(self):
    #     """
    #     Возвращает детализированную информацию о содержимом корзины и общей стоимости.
    #     """
    #     details = "Корзина покупок:\n"
    #     for item in self.items:
    #         details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
    #     details += f"Общее: {self.get_total()} руб"
    #     return details
    

    def get_details(self, user, payment_receipt_status ):   #dict{username : payment}
        """
        Возвращает информацию о содержимом корзины, общей стоимости и статусу оформления заказа.
        """
        details = ""
        for item in self.items:
            details += f"{item['Продукт'].name} * {item['количество']} шт, "
        details += f"на общую сумму: {self.get_total()} руб "
    
        if payment_receipt_status == 'success':
            return f'{user.username} приобрел : ' + details + '- зарегистрировал покупки пользователь админ'
        else: 
            return ' заказ неоплачен '
        