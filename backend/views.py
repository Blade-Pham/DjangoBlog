from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, ProjectSerializer, NewsSerializer
from .services.newsService import NewsService
from .services.projectService import ProjectService
from .services.userService import UserService


# Create your views here.
class UserListView(APIView):
    # @api_view(['GET'])
    def get(self,request):
        try:
            users = UserService.list_users()
            if not users:  # Nếu danh sách rỗng
                return Response({"error": "Không có người dùng nào"}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                new_user = UserService.create_user(serializer.data)
                return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user=UserService.get_user(pk)
            if not user:
                return Response({"error": "Không có người dùng nào"}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            user = UserService.get_user(pk)
            if not user:
                return Response({"error": "Không có người dùng nào"}, status=status.HTTP_404_NOT_FOUND)
            UserService.delete_user(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            new_user = UserService.update_user(pk, request.data)
            if new_user:
                return Response(UserSerializer(new_user).data, status=status.HTTP_200_OK)
            return Response({"error": "Không có người dùng nào"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectListView(APIView):
    # @api_view(['GET'])
    def get(self,request):
        try:
            projects = ProjectService.list_projects()
            if not projects:  # Nếu danh sách rỗng
                return Response({"error": "Không có dự án nào"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self, request):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                new_project = ProjectService.create_project(serializer.data)
                return Response(ProjectSerializer(new_project).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ProjectDetailView(APIView):
    def get(self, request, pk):
        try:
            project=ProjectService.get_project(pk)
            if not project:
                return Response({"error": "Không có dự án nào"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            project = ProjectService.get_project(pk)
            if not project:
                return Response({"error": "Không có dự án nào"}, status=status.HTTP_404_NOT_FOUND)
            ProjectService.delete_project(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            new_project = ProjectService.update_project(pk, request.data)
            if new_project:
                return Response(ProjectSerializer(new_project).data, status=status.HTTP_200_OK)
            return Response({"error": "Không có dự án nào"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NewsListView(APIView):
    # @api_view(['GET'])
    def get(self,request):
        try:
            newss = NewsService.list_newss()
            if not newss:  # Nếu danh sách rỗng
                return Response({"error": "Không có tin tức nào"}, status=status.HTTP_404_NOT_FOUND)
            serializer = NewsSerializer(newss, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = NewsSerializer(data=request.data)
            if serializer.is_valid():
                new_news = NewsService.create_news(serializer.data)
                return Response(NewsSerializer(new_news).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class NewsDetailView(APIView):
    def get(self, request, pk):
        try:
            news=NewsService.get_news(pk)
            if not news:
                return Response({"error": "Không có tin tức nào"}, status=status.HTTP_404_NOT_FOUND)
            serializer = NewsSerializer(news)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            news = NewsService.get_news(pk)
            if not news:
                return Response({"error": "Không có tin tức nào"}, status=status.HTTP_404_NOT_FOUND)
            NewsService.delete_news(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            new_news = NewsService.update_news(pk, request.data)
            if new_news:
                return Response(NewsSerializer(new_news).data, status=status.HTTP_200_OK)
            return Response({"error": "Không có tin tức nào"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "Lỗi máy chủ nội bộ", "details": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)