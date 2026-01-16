# Django Chat API

A secure and scalable chat API built with Django REST Framework and JWT authentication.

## Features

- 🔐 **JWT Authentication** - Secure token-based authentication
- 👤 **User Management** - Registration, login, and profile management
- 💬 **Real-time Chat** - Create and manage conversations and messages
- ⚡ **Rate Limiting** - Protect your API from abuse
- 🔒 **Password Validation** - Strong password requirements
- 🌐 **CORS Support** - Configure allowed origins via environment variables
- 🐳 **Docker Support** - Easy deployment with Docker and docker-compose

## Prerequisites

- Python 3.8+
- PostgreSQL
- Docker and Docker Compose (optional)
- pip

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd django/core
```

### 2. Set up environment variables

Copy the example environment file and update the values:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration:

```env
# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Django
DEBUG=True
SECRET_KEY=your-secret-key-here
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# CORS Settings
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOW_CREDENTIALS=True
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT tokens
- `POST /api/auth/token/refresh/` - Refresh access token
- `POST /api/auth/logout/` - Logout and blacklist refresh token

### Conversations

- `POST /api/conversation/newconversation/` - Create a new conversation
- `POST /api/conversation/message/` - Send a message in a conversation
- `DELETE /api/conversation/deleteconversation/{id}/` - Delete a conversation

## Running with Docker

1. Make sure Docker and Docker Compose are installed
2. Update the `.env` file with your database credentials
3. Run:

```bash
docker-compose up --build
```

## Project Structure

```
core/
├── accounts/                 # User authentication and profiles
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── signals.py
│   ├── throttles.py
│   ├── urls.py
│   └── views.py
│
├── conversation/             # Chat functionality
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── core/                     # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .env.example             # Example environment variables
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── README.md
└── requirements.txt
```

## Security

- JWT token-based authentication
- Password hashing using PBKDF2 with SHA256
- Rate limiting on authentication endpoints
- CORS protection
- Secure password validation
- CSRF protection

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL
- Docker

## Support

For support, please open an issue in the GitHub repository.
