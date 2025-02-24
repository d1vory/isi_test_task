from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.serializers.login import LoginSerializer


class LoginView(GenericAPIView):
    queryset =  User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')

        user = self.get_queryset().filter(username=username).first()
        if not user:
            raise ValidationError('Wrong credentials')
        if not user.check_password(password):
            raise ValidationError('Wrong credentials')
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response({'token': f'{token}'})