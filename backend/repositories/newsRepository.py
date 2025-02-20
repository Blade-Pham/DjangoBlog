from ..models import News

class NewsRepository:
    @staticmethod
    def get_all():
        return News.objects.all()
    def get_by_id(id):
        return News.objects.filter(id=id).first()
    def create(news):
        return News.objects.create(**news)
    def delete(id):
        return News.objects.get(id=id).delete()
    def update(news, data):
        for key, value in data.items():
            setattr(news, key, value)
        news.save()
        return news