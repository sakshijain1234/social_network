# friends/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer
from .models import FriendRequest
from .serializers import FriendRequestSerializer
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status

class FriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        from_user = self.request.user
        to_user = self.request.data.get('to_user')
        
        if from_user.blocked_users.filter(id=to_user.id).exists():
            return Response({"error": "You are blocked by this user."}, status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            serializer.save(from_user=from_user, to_user=to_user)

class AcceptFriendRequestView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.status = 'accepted'
        friend_request.save()
        return Response({'status': 'Friend request accepted'})

class FriendsListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return user.friends.all()

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        # Get the pending friend requests received by the logged-in user
        user = self.request.user
        return FriendRequest.objects.filter(receiver=user, status='pending') 

