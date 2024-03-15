from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User

from rest_framework.response import Response

from .serializers import UserSerializer

from django.contrib.auth import authenticate, login, logout

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({
                "meessage": "로그인 성공"
            }, status=200)
        else:
            return Response({
                "message": "로그인 실패"
            }, status=401)

class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({
            "message": "로그아웃 성공"
        }, status=200)