from user import Customer, Admin
import uuid


class AuthenticationService:

    def __init__ (self):
        self.session_token = dict()

    def register (self, user_class, username, email, password, **kvargs ):
        """Регистрация пользователя с проверкой уникальности имени возвращает экземпляр класса Customer или Admin"""
        if username in user_class.users:
            return print('имя занято, выберете другое')
        else:
            user = user_class(username=username, email=email, password=password, **kvargs )
            print(f'Зарегистрирован пользователь {user.username}') 
            return user
    
    def login (self, user_class, username, password):
        """вход в сервис с помощью проверки логина и пароля для зарегистрированного пользователя и создание токена старта сессии"""
        if username in user_class.users and username == user_class.username and user_class.password == user_class.hash_password(password):
            self.session_token[user_class.username] = uuid.uuid4()
            return print(username , ' вход выполнен')
        else:
            return print('повторите попытку')


    def logout (self, username):
        """вход из сервиса, удаление токена старта сессии"""
        del self.session_token[username]
        return print(username , ' выход выполнен')
        

    def get_current_user(self):
        """получение списка активных пользователей сервиса"""
        if self.session_token:
            print(f'активныe сессии: {list(self.session_token.keys())}') 
        else:
            print('активных сессий нет')





