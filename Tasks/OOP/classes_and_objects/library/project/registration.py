from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)
        return None

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        
