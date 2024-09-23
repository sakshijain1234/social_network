# users/views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import User, UserSerializer, CustomTokenObtainPairSerializer,UserActivitySerializer
from .models import UserActivity  # Assuming you have a UserActivity model 

# User Signup
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# User Login (JWT)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        if query:
            return User.objects.filter(username__icontains=query) | User.objects.filter(email__icontains=query)
        return User.objects.none()
    
class BlockUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_to_block_email = request.data.get('email')

        if not user_to_block_email:
            return Response({'error': 'Email of the user to block is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_to_block = User.objects.get(email=user_to_block_email)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Block the user
        request.user.blocked_users.add(user_to_block)

        return Response({'success': f'User {user_to_block_email} has been blocked.'}, status=status.HTTP_200_OK)
    
class UserActivityView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can view activity
    serializer_class = UserActivitySerializer

    def get_queryset(self):
        # Get the activities of the logged-in user
        user = self.request.user
        return UserActivity.objects.filter(user=user).order_by('-timestamp')  # Assuming a 'timestamp' field

