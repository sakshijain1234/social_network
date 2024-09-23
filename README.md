﻿# social_network

 hello coders,

installation steps:

# Clone the repository
git clone <your-repo-link>

# Navigate into the project directory
cd social_network

# Install dependencies
pip install -r requirements.txt

# Run the project
python manage.py runserver

1. Project Overview
The Social Networking API allows users to:

Sign up and log in with email and password (case-insensitive login).
Send, accept, and reject friend requests.
Manage friend lists and view pending friend requests.
Search for users by name.
Block/unblock users.
Track user activities (e.g., friend requests, rejections).
Implement role-based access control (RBAC) for different user roles: Admin, Write, and Read

2. Architectural Design
2.1. Backend Framework
Django: Chosen for its robustness, built-in admin capabilities, and scalability in web application development.
Django Rest Framework (DRF): For API design and implementation, DRF provides out-of-the-box support for authentication, serialization, and request validation.
PostgreSQL: The relational database was chosen for its scalability, ACID compliance, and support for full-text search, which optimizes search functionality for large datasets.

2.2. Horizontal Scalability
Docker: Dockerized the application to enable smooth scaling by easily running multiple instances of the app across multiple servers.
Database: PostgreSQL allows horizontal partitioning and sharding to handle large-scale data.
Load Balancing: Designed to support load balancing across multiple server instances if needed

3. Database Design
3.1. Key Entities
User: Custom User model extending Django’s AbstractUser. The model contains user-specific fields such as role, email, and blocked_users.
FriendRequest: Tracks friend requests between users and their current status (pending, accepted, rejected).
UserActivity: Logs user activity for auditing and notifications.
3.2. Table Structure
User Table: Contains user-specific information like email (unique), role, and relationships for blocking other users.
FriendRequest Table: Stores sender (from_user) and recipient (to_user) user IDs along with the status of the request (pending, accepted, rejected).
UserActivity Table: Records activities (e.g., friend requests sent or accepted) with timestamps and user references.

4. API Design Choices
4.1. Authentication & Authorization
Role-Based Access Control (RBAC): Implemented via a role field in the User model. Admins have full CRUD access, while Write users can create content, and Read users have limited access.
Rate Limiting: Applied to login and friend request endpoints to prevent brute force attacks and spam requests. Limiting logins mitigates the risk of account compromise.
4.2. API Endpoints
Login/Signup:
Simple username,email and password-based login/signup (no OTP).
Email is case-insensitive for both login and signup.
Friend Request Management:
Users can send, accept, or reject friend requests. Users can send a maximum of 3 requests per minute to prevent spamming.
Atomic operations to handle race conditions in accepting/rejecting friend requests.
A 24-hour cooldown period is enforced after a friend request is rejected.
User Search:
Uses PostgreSQL full-text search for optimized searching by email or name.

api documentation:

social_network
These are the api documentation for social networking

http://127.0.0.1:8000/api/signup/
http://127.0.0.1:8000/api/login/
http://127.0.0.1:8000/api/users/search/?query=<name>
http://127.0.0.1:8000/api/friends/friend-request/
http://127.0.0.1:8000/api/friends/friend-request/accept/
http://127.0.0.1:8000/api/friends/list/
http://127.0.0.1:8000/api/friends/requests/pending/
http://127.0.0.1:8000/api/users/block/
http://127.0.0.1:8000/api/users/activity/






