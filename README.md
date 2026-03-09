# E-commerce Product REST API

## Project Overview
This repository contains a RESTful API designed to manage an e-commerce product catalog. The system is built using the Django framework and Django REST Framework (DRF), providing a scalable backend for product management, user authentication, and advanced data filtering.

## Technical Specifications
- **Framework**: Django 5.x
- **API Engine**: Django REST Framework
- **Authentication**: JWT (JSON Web Tokens) via SimpleJWT
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Data Filtering**: Django-filter

## Functional Requirements
- **Product Management**: Full CRUD operations for products and categories.
- **User Management**: Registration and authentication for administrative access.
- **Search Logic**: Partial name matching and description search functionality.
- **Filtering**: Query parameters for category, price range, and stock availability.
- **Pagination**: Standardized response limits for performance optimization.

## API Documentation

### Authentication Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /api/token/ | Obtain access and refresh tokens |
| POST | /api/token/refresh/ | Generate new access token |

### Product Endpoints
| Method | Endpoint | Access Control |
| :--- | :--- | :--- |
| GET | /api/products/ | Public |
| POST | /api/products/ | Authenticated Staff Only |
| GET | /api/products/<id>/ | Public |
| PUT/PATCH | /api/products/<id>/ | Authenticated Staff Only |
| DELETE | /api/products/<id>/ | Authenticated Staff Only |

## Installation and Configuration

### 1. Environment Setup
Clone the repository and initialize the virtual environment:
```bash
git clone [https://github.com/AhmedFakhr999/e-commerce_back_end.git](https://github.com/AhmedFakhr999/e-commerce_back_end.git)
cd e-commerce_back_end
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
