# E-Commerce Platform

A full-featured e-commerce platform built with Django REST Framework backend and Next.js frontend.

## Stack

- **Frontend**: Next.js 14
- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL
- **Cache/Sessions**: Redis
- **Task Queue**: Celery
- **Deployment**: Docker & Docker Compose

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git

### Setup

1. Clone the repository:
```bash
git clone <repo-url>
cd e-commerce
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Start the project with Docker Compose:
```bash
docker-compose up -d
```

4. Run migrations:
```bash
docker-compose exec django python manage.py migrate
```

5. Create a superuser:
```bash
docker-compose exec django python manage.py createsuperuser
```

6. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api
- Admin: http://localhost:8000/admin

## Project Structure

```
e-commerce/
├── backend/
│   ├── ecommerce/
│   │   ├── config/          # Django settings & URLs
│   │   ├── apps/            # Django applications
│   │   │   ├── accounts/    # User authentication
│   │   │   ├── catalog/     # Products & categories
│   │   │   ├── cart/        # Shopping cart
│   │   │   ├── checkout/    # Checkout flow
│   │   │   ├── orders/      # Order management
│   │   │   ├── payments/    # Payment processing
│   │   │   ├── shipping/    # Shipping management
│   │   │   ├── promotions/  # Discounts & coupons
│   │   │   ├── reviews/     # Product reviews
│   │   │   ├── support/     # Customer support
│   │   │   └── analytics/   # Analytics
│   │   ├── templates/
│   │   ├── static/
│   │   └── media/
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── app/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/
│   │   ├── styles/
│   │   └── (pages structure)
│   ├── package.json
│   └── next.config.js
├── docker/
│   ├── Dockerfile.django
│   └── Dockerfile.nextjs
└── docker-compose.yml
```

## Development

### Backend Development

```bash
# Install dependencies
cd backend
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver

# Run Celery (in another terminal)
celery -A ecommerce.config worker -l info
```

### Frontend Development

```bash
# Install dependencies
cd frontend
npm install

# Start development server
npm run dev
```

## API Endpoints

- `/api/auth/` - Authentication
- `/api/products/` - Products & Categories
- `/api/cart/` - Shopping Cart
- `/api/checkout/` - Checkout
- `/api/orders/` - Orders
- `/api/payments/` - Payments
- `/api/shipping/` - Shipping
- `/api/promotions/` - Promotions & Coupons
- `/api/reviews/` - Product Reviews
- `/api/support/` - Support & Help
- `/api/analytics/` - Analytics

## Database Schema

Key tables:
- users, profiles, addresses
- categories, products, product_variants, product_images
- inventory, carts, cart_items
- orders, order_items
- payments, shipments
- coupons, reviews, wishlist, returns

## Next Steps

1. Implement authentication endpoints
2. Create product catalog with filtering
3. Build shopping cart functionality
4. Implement checkout and payment processing
5. Set up order management
6. Create admin dashboard
7. Add analytics tracking
8. Deploy to production

## License

MIT
"# E-Commerce" 
