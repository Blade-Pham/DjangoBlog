from ..repositories.userRepository import UserRepository


class UserService:
    @staticmethod
    def list_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user(id):
        return UserRepository.get_by_id(id)
    def create_user(user):
        return UserRepository.create(user)
    def delete_user(id):
        return UserRepository.delete(id)
    def update_user(id, data):
        new_user = UserRepository.get_by_id(id)
        if new_user:
            return UserRepository.update(new_user, data)
        return None