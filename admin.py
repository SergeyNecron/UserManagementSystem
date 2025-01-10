from user import User

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')  # Администраторы имеют уровень доступа 'admin'
        self.__users = []  # Список пользователей (только для администраторов)

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"User {user.get_name()} added by admin {self.get_name()}")
        else:
            print("Invalid user object")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_id() == user_id:
                self.__users.remove(user)
                print(f"User {user.get_name()} removed by admin {self.get_name()}")
                return True
        print("User not found")
        return False

    def get_users(self):
        user_names = [user.get_name() for user in self.__users]
        return user_names

