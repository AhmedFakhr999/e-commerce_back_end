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



# E-commerce Product REST API - Week 2 Progress

## Current Implementation Status
The project has moved into Phase 2. The core API endpoints for Product and Category management are now functional.

## Accomplishments (Week 2)
- **RESTful Serialization**: Implemented `ModelSerializers` to handle JSON data validation and formatting.
- **API ViewSets**: Developed `ModelViewSets` to provide standardized CRUD functionality.
- **Routing**: Established a dynamic URL routing system using DRF Routers.
- **Database Optimization**: Utilized `select_related` on product queries to minimize database hits.

## API Endpoint Reference
| Method | Endpoint | Description | Status |
| :--- | :--- | :--- | :--- |
| GET | `/api/products/` | List all products | Functional |
| POST | `/api/products/` | Create a product | Functional |
| GET | `/api/categories/` | List all categories | Functional |
| PATCH | `/api/products/<id>/` | Update product details | Functional |

## Installation & Testing
1. Ensure the virtual environment is active.
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Access the browsable API at: `http://127.0.0.1:8000/api/products/`

## Roadmap
- [x] Week 1: Models and Admin Setup
- [x] Week 2: CRUD Serializers and ViewSets
- [ ] Week 3: Authentication and Permissions (JWT)
- [ ] Week 4: Search and Filtering Logic
- [ ] Week 5: Deployment