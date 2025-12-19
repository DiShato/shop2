from user import Customer, Admin
from authentication import AuthenticationService

# Пабота сервиса--------------------------------
# Запустим сервис
auth_service = AuthenticationService()

# Регистрируем пользователей
user1 = auth_service.register(Customer, username="Alin", email="python@gmail.ru", password='vgbhjnomkp,l', address="042 Russ Kem")
user2 = auth_service.register(Customer, username="Alin", email="python@gmail.ru", password='vgbhjnomkp,l', address="042 Russ Kem")
user2 = auth_service.register(Customer, username="Alina", email="python@gmail.ru", password='vgbhjnomkp,l', address="042 Russ Kem")
admin = auth_service.register(Admin, username="root", email="root@gmail.ru", password='dfygyuhjioklkijuhgvfcdxc', admin_level=5)
print()

# Пользователи заходят на платформу 
auth_service.login(user1, username="Alin", password='vgbhjnomkp,l')
auth_service.login(user2, username="Alina", password='vgbhjnomkp,l')
auth_service.login(admin, username="root", password='dfygyuhjioklkijuhgvfcdxc')
print()

# просмотр активных сессий
print('токены сессий: ', auth_service.session_token) 
print(auth_service.get_current_user())
print()

# выход из сервиса
auth_service.logout("Alin")
auth_service.logout("Alina")
print(auth_service.get_current_user())
print()

# возможности админа----------------------------
# просмотр списка пользователей
list_users = admin.list_users()
print('list_users: ', list_users)
print()

# удаление пользоватея
admin.del_user("Alin")
list_users = admin.list_users()
print('list_users: ', list_users)
auth_service.login(user1, username="Alin", password='vgbhjnomkp,l') #теперь пользователь не может зайти
print()