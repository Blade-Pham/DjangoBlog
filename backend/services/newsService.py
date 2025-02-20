from ..repositories.newsRepository import NewsRepository
from ..repositories.userRepository import UserRepository


class NewsService:
    @staticmethod
    def list_newss():
        return NewsRepository.get_all()

    @staticmethod
    def get_news(id):
        return NewsRepository.get_by_id(id)
    def create_news(news):
        user_id =news.get("user")
        user_instance = UserRepository.get_by_id(user_id)
        if user_instance:
            news["user"] = user_instance
            return NewsRepository.create(news)
        return None
    def delete_news(id):
        return NewsRepository.delete(id)
    def update_news(id, data):
        new_news = NewsRepository.get_by_id(id)
        if new_news:
            return NewsRepository.update(new_news, data)
        return None