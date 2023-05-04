from django.contrib.auth import get_user_model, login
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, ArraySerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)

class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_user_model().objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class MaxMinView(generics.GenericAPIView):
    serializer_class = ArraySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = ArraySerializer(data=request.data)
        if serializer.is_valid():
            array = serializer.validated_data['array']
            return Response({'max': max(array), 'min': min(array)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
