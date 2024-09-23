# friends/urls.py
from django.urls import path
from .views import FriendRequestView, AcceptFriendRequestView
from .views import FriendsListView,PendingFriendRequestsView

urlpatterns = [
    path('friend-request/', FriendRequestView.as_view(), name='send_friend_request'),
    path('friend-request/accept/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('list/', FriendsListView.as_view(), name='friends-list'),
    path('requests/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
]
