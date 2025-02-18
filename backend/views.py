from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
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