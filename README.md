Online Cinema

An online cinema platform built with FastAPI, allowing users to browse, purchase, and rate movies. Features include JWT-based authentication, role-based access, shopping cart, orders, payments integration, and Dockerized deployment.

Features
1. Authorization & Authentication

User Registration:

Users register using email and receive an activation link valid for 24 hours.

Can resend activation link if expired.

Email uniqueness enforced.

Login & Logout:

JWT access and refresh tokens issued upon login.

Logout deletes the refresh token.

Password Management:

Change password (requires old password).

Reset forgotten password via email token.

Password complexity validation enforced.

User Groups & Permissions:

USER – Basic access.

MODERATOR – Can manage movies, view sales.

ADMIN – Can manage users, groups, and activate accounts manually.

2. Movies

Browse catalog with pagination, filtering, and sorting.

View detailed movie info, like/dislike, comment, rate (1-10).

Search by title, description, actor, director.

Favorite movies and perform catalog functions on favorites.

Moderators can perform CRUD operations on movies, genres, and actors.

Prevent deletion of movies purchased by users.

3. Shopping Cart

Users can add/remove movies in their cart.

Prevent duplicate or already purchased movies.

View cart with movie details (title, genre, price, release year).

Clear cart manually.

Moderators can view users’ carts for analysis.

4. Orders

Place orders for movies in cart.

Exclude unavailable or already purchased movies.

View order history: date, movies, total amount, status (pending, paid, canceled).

Cancel pending orders; refunds possible after payment.

Email confirmation on successful payment.

Admins can filter orders by users, dates, and status.

5. Payments

Stripe integration for payments.

View payment history: date, amount, status (successful, canceled, refunded).

Payment validation through Stripe webhooks.

Admins can filter payments by users, dates, and status.

Detailed payment items ensure accurate financial reporting.

6. Docker & Docker Compose

Containerized project for easy deployment.

Services included: FastAPI, Redis, Celery, MinIO.

Single command to launch all services.

Tech Stack

Backend: FastAPI, Pydantic, SQLAlchemy

Database: PostgreSQL (or your preferred relational DB)

Asynchronous Tasks: Celery + Redis

Storage: MinIO for avatars and media

Authentication: JWT (access + refresh tokens)

Payments: Stripe

Containerization: Docker, Docker Compose

Installation

Clone the repository:

git clone https://github.com/yourusername/online-cinema.git
cd online-cinema

Copy .env.example to .env and configure environment variables:

cp .env.example .env

Build and run Docker containers:

docker-compose up --build
