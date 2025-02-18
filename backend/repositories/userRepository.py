from ..models import User


class UserRepository:
    @staticmethod
    def get_all():
        return User.objects.all()
    def get_by_id(id):
        return User.objects.filter(id=id).first()
    def create(user):
        return User.objects.create(**user)
    def delete(id):
        return User.objects.get(id=id).delete()
    def update(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user