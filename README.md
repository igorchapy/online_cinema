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

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/online-cinema.git
cd online-cinema
