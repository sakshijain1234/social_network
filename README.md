<h1>Social Network</h1>

<p>Hello Coders,</p>

<h2>Installation Steps:</h2>

<ol>
  <li><b>Clone the repository:</b><br>
    <code>git clone &lt;your-repo-link&gt;</code>
  </li>
  <li><b>Navigate into the project directory:</b><br>
    <code>cd social_network</code>
  </li>
  <li><b>Install dependencies:</b><br>
    <code>pip install -r requirements.txt</code>
  </li>
  <li><b>Run the project:</b><br>
    <code>python manage.py runserver</code>
  </li>
</ol>

<h2>1. Project Overview</h2>
<p>The Social Networking API allows users to:</p>
<ul>
  <li>Sign up and log in with username,email and password (case-insensitive login).</li>
  <li>Send, accept, and reject friend requests.</li>
  <li>Manage friend lists and view pending friend requests.</li>
  <li>Search for users by name.</li>
  <li>Block/unblock users.</li>
  <li>Track user activities (e.g., friend requests, rejections).</li>
  <li>Implement role-based access control (RBAC) for different user roles: Admin, Write, and Read.</li>
</ul>

<h2>2. Architectural Design</h2>

<h3>2.1. Backend Framework</h3>
<ul>
  <li><b>Django:</b> Chosen for its robustness, built-in admin capabilities, and scalability in web application development.</li>
  <li><b>Django Rest Framework (DRF):</b> For API design and implementation, DRF provides out-of-the-box support for authentication, serialization, and request validation.</li>
  <li><b>PostgreSQL:</b> The relational database was chosen for its scalability, ACID compliance, and support for full-text search, which optimizes search functionality for large datasets.</li>
</ul>

<h3>2.2. Horizontal Scalability</h3>
<ul>
  <li><b>Docker:</b> Dockerized the application to enable smooth scaling by easily running multiple instances of the app across multiple servers.</li>
  <li><b>Database:</b> PostgreSQL allows horizontal partitioning and sharding to handle large-scale data.</li>
  <li><b>Load Balancing:</b> Designed to support load balancing across multiple server instances if needed.</li>
</ul>

<h2>3. Database Design</h2>

<h3>3.1. Key Entities</h3>
<ul>
  <li><b>User:</b> Custom User model extending Django’s AbstractUser. The model contains user-specific fields such as role, email, and blocked_users.</li>
  <li><b>FriendRequest:</b> Tracks friend requests between users and their current status (pending, accepted, rejected).</li>
  <li><b>UserActivity:</b> Logs user activity for auditing and notifications.</li>
</ul>

<h3>3.2. Table Structure</h3>
<ul>
  <li><b>User Table:</b> Contains user-specific information like email (unique), role, and relationships for blocking other users.</li>
  <li><b>FriendRequest Table:</b> Stores sender (<code>from_user</code>) and recipient (<code>to_user</code>) user IDs along with the status of the request (pending, accepted, rejected).</li>
  <li><b>UserActivity Table:</b> Records activities (e.g., friend requests sent or accepted) with timestamps and user references.</li>
</ul>

<h2>4. API Design Choices</h2>

<h3>4.1. Authentication & Authorization</h3>
<ul>
  <li><b>Role-Based Access Control (RBAC):</b> Implemented via a role field in the User model. Admins have full CRUD access, while Write users can create content, and Read users have limited access.</li>
  <li><b>Rate Limiting:</b> Applied to login and friend request endpoints to prevent brute force attacks and spam requests. Limiting logins mitigates the risk of account compromise.</li>
</ul>

<h3>4.2. API Endpoints</h3>
<ul>
  <li><b>Login/Signup:</b><br>
    Simple username, email, and password-based login/signup (no OTP).<br>
    Email is case-insensitive for both login and signup.
  </li>
  <li><b>Friend Request Management:</b><br>
    Users can send, accept, or reject friend requests. Users can send a maximum of 3 requests per minute to prevent spamming.<br>
    Atomic operations to handle race conditions in accepting/rejecting friend requests.<br>
    A 24-hour cooldown period is enforced after a friend request is rejected.
  </li>
  <li><b>User Search:</b><br>
    Uses PostgreSQL full-text search for optimized searching by email or name.
  </li>
</ul>

<h2>API Documentation</h2>

<p>These are the API documentation for social networking:</p>

<ul>
  <li>Signup API: http://127.0.0.1:8000/api/signup/</li>
<li>Login API: http://127.0.0.1:8000/api/login/</li>
<li>User Search API: http://127.0.0.1:8000/api/users/search/?query=<name></li>
<li>Send Friend Request API: http://127.0.0.1:8000/api/friends/friend-request/</li>
<li>Accept Friend Request API: http://127.0.0.1:8000/api/friends/friend-request/accept/</li>
<li>Friend List API: http://127.0.0.1:8000/api/friends/list/</li>
<li>Pending Friend Requests API: http://127.0.0.1:8000/api/friends/requests/pending/</li>
<li>Block User API: http://127.0.0.1:8000/api/users/block/</li>
<li>User Activity API: http://127.0.0.1:8000/api/users/activity/</li>

</ul>

<p>See the: <a href="https://elements.getpostman.com/redirect?entityId=34643816-fd3203ac-cad5-4bc3-8cb6-5896bdd18d54&entityType=collection">Postman Collection Link</a>
</p>







