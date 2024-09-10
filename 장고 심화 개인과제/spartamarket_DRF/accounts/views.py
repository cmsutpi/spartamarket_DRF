from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .validators import validate_user_data

class UserCreateView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        rlt_message = validate_user_data(request.data)
        if rlt_message is not None:
            return Response({"message": rlt_message}, status=400)

        username = request.data.get("username")
        password = request.data.get("password")
        nickname = request.data.get("nickname")
        birth = request.data.get("birth")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")

        if len(nickname) < 4:
            return Response(
                {"message: 닉네임은 4자 이상이어야 합니다."}
                status=400,
            )
        

        validate_user_data(request.data)

        user = User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname,
            birth=birth,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        return Response(
            {
                "id": user.pk,
                "username": user.username,
                "nickname": user.nickname,
                "email": user.email,
            }
    )

        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {"message": "아이디 또는 비밀번호가 틀렸습니다."}
            status=400,
            )
            
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh":str(refresh),
                "access": str(refresh.access_token),
            }
        )
        
class UserProfileView(APIView):

    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)