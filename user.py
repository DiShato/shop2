import hashlib

class User:

    """Базовый класс, представляющий пользователя."""

    users = set()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = User.hash_password(password)
        User.users.add(self.username)

    
    def get_details(self):
        """Вывод деталей экзампляра класса пользователя"""    
        return print(f'username : {self.username}, email: {self.email}')
    
    
    @staticmethod
    def hash_password(password):
        """Возвращает хэшированное значение пароля"""
        hash_pass = hashlib.sha1(str(password).encode("UTF-8")).hexdigest()
        return hash_pass
    
    
    @staticmethod
    def check_password(stored_password, provided_password):
        """Проверка правильность введенного пароля"""
        if stored_password  == User.hash_password(provided_password):
            
            return print('Проверка пароля пройдена')
        else:
            return print('Проверка пароля не пройдена')




class Customer(User):

    """Класс, представляющий клиента, наследующий класс User."""

    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        """Вывод деталей экзампляра класса Customer"""    
        return print(f'username : {self.username}, address: {self.address}')
    


class Admin(User):

    """Класс, представляющий Admin, наследующий класс User."""

    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        """Вывод деталей экзампляра класса Admin"""
        return print(f'Admin : {self.username}, admin_level: {self.admin_level}')
    
    @staticmethod
    def list_users():
        """Вывод списка пользователей"""
        return list(User.users)

    @staticmethod
    def del_user(username):
        """Удаление пользователя по имени"""
        User.users.discard(username)
        print(f"пользователь {username} удален") 
