from user import User
from admin import  Admin

if __name__ == "__main__":
    # Пример использования:
    user1 = User(1, "Alice")
    admin = Admin(2, "Bob")

    print(f"User {user1.get_name()} - ID: {user1.get_id()}, Access Level: {user1.get_access_level()}")
    print(f"Admin {admin.get_name()} - Access Level: {admin.get_access_level()}")

    admin.add_user(user1)
    print("Users in system:", admin.get_users())

    admin.remove_user(0)
    print("Users in system after removal:", admin.get_users())
