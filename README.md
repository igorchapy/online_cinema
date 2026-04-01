# 🎬 Online Cinema

An **online cinema platform** built with **FastAPI**, allowing users to browse, purchase, and rate movies.

The system includes authentication, role-based access control, shopping cart, orders, Stripe payments, and full Dockerized deployment.

---

## 🚀 Features

### 🎥 Movies

- Browse catalog with:
  - Pagination
  - Filtering
  - Sorting
- Movie details:
  - Description, actors, director
  - Ratings (1–10)
  - Comments, likes/dislikes
- Search by:
  - Title
  - Description
  - Actor / Director
- Favorites system:
  - Save and manage favorite movies

**Moderator capabilities:**
- CRUD operations for:
  - Movies
  - Genres
  - Actors
- Prevent deletion of purchased movies

---

### 🛒 Shopping Cart

- Add/remove movies
- Prevent:
  - Duplicate items
  - Already purchased movies
- View cart with:
  - Title
  - Genre
  - Price
  - Release year
- Clear cart manually

**Moderator access:**
- View users' carts for analytics

---

### 📦 Orders

- Create orders from cart
- Automatically exclude:
  - Unavailable movies
  - Already purchased movies
- Order history:
  - Date
  - Movies
  - Total amount
  - Status (`pending`, `paid`, `canceled`)
- Cancel pending orders
- Refund support after payment
- Email confirmation on payment

**Admin capabilities:**
- Filter orders by:
  - User
  - Date
  - Status

---

### 💳 Payments

- Integration with **Stripe**
- Payment tracking:
  - Date
  - Amount
  - Status (`successful`, `canceled`, `refunded`)
- Stripe webhooks for validation
- Detailed payment items for financial accuracy

**Admin capabilities:**
- Filter payments by:
  - User
  - Date
  - Status

---

### 🐳 Docker & Deployment

- Fully containerized setup
- Services included:
  - FastAPI
  - PostgreSQL
  - Redis
  - Celery
  - MinIO
- One-command startup

---

## 🧰 Tech Stack

| Category              | Technology              |
|----------------------|------------------------|
| Backend              | FastAPI, Pydantic      |
| ORM                  | SQLAlchemy             |
| Database             | PostgreSQL             |
| Async Tasks          | Celery + Redis         |
| Storage              | MinIO                  |
| Authentication       | JWT                    |
| Payments             | Stripe                 |
| Containerization     | Docker, Docker Compose |

---

1️⃣ Make sure Docker and Docker Compose are installed

Check versions:

docker --version
docker-compose --version

If you don’t have them installed:

Windows/Mac → Install Docker Desktop
Linux → Install Docker Engine + Docker Compose
2️⃣ Go to your project directory
cd online-cinema
3️⃣ Build Docker images

If you have a docker-compose.yml that defines all services (FastAPI, PostgreSQL, Redis, Celery, MinIO, etc.):

docker-compose build

This will build all the project images.

4️⃣ Run the containers
docker-compose up
To run in the background (detached mode):
docker-compose up -d
5️⃣ Check logs and container status
Follow logs:
docker-compose logs -f
See running containers:
docker ps
6️⃣ Stop containers
docker-compose down
This stops and removes all containers. Data in volumes is preserved.
⚡ Tips
Make sure ports are mapped correctly in docker-compose.yml:
ports:
  - "8000:8000"  # FastAPI
If FastAPI uses Uvicorn, make sure the command in docker-compose.yml is:
command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
On Windows, sometimes volume permissions can cause permission denied errors—make sure file sharing is enabled for the project folder.