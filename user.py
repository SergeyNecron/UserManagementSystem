class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__id = user_id  # Уникальный идентификатор пользователя
        self.__name = name  # Имя пользователя
        self.__access_level = access_level  # Уровень доступа (по умолчанию 'user')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level
