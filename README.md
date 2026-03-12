# Centribal API

REST API built with **Django** and **Django REST Framework** to manage **articles** and **orders**.
The project follows **Hexagonal Architecture (Ports & Adapters)** to separate domain logic from infrastructure.

---

## Tech Stack

* Python 3.11
* Django
* Django REST Framework
* PostgreSQL
* Docker
* Pytest
* Swagger / OpenAPI documentation

---

## Run the Project

Start the containers:

```
docker-compose up --build
```

The application will run at:

```
http://localhost:8000
```

Database migrations are executed automatically when the container starts.

---

## Create an Admin User

To access the Django admin panel, create a superuser:

```
docker-compose exec api python manage.py createsuperuser
```

Then open:

```
http://localhost:8000/admin/
```

Login with the credentials you just created.

---

## API Documentation

Interactive API documentation is available via Swagger:

```
http://localhost:8000/api/docs/
```

OpenAPI schema:

```
http://localhost:8000/api/schema/
```

---

## Main Endpoints

### Articles

```
GET    /api/articles/
GET    /api/articles/{id}/
POST   /api/articles/
PUT    /api/articles/{id}/
```

### Orders

```
GET    /api/orders/
GET    /api/orders/{id}/
POST   /api/orders/
PUT    /api/orders/{id}/
```

---

## Run Tests

Execute unit tests with:

```
pytest
```

Tests cover the **application use cases** using in-memory repositories.
