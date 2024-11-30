import logging
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from .models import CustomUser

logger = logging.getLogger(__name__)

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User {request.user.username} logged out successfully.")
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.error(f"Error during logout: {e}")
            return Response(status=status.HTTP_400_BAD_REQUEST)