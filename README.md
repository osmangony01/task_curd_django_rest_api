# Django REST API - Task Management System

A complete Django REST API project for task management with full CRUD operations, Swagger documentation, and modern development practices.

## 🚀 Features

- **Full CRUD Operations**: Create, Read, Update, Delete tasks
- **RESTful API Design**: Following REST principles
- **Swagger Documentation**: Interactive API documentation with drf-yasg
- **Environment Configuration**: Secure configuration with python-decouple
- **Database Support**: SQLite for development, PostgreSQL for production
- **Modular Architecture**: Clean app structure with separation of concerns
- **Error Handling**: Comprehensive error responses
- **Data Validation**: Django REST Framework serializers

## 📁 Project Structure

```
django_rest_api_project/
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database file
├── README.md                    # Project documentation
├── .env                         # Environment variables (create this)
├── requirements.txt             # Python dependencies (create this)
│
├── config/                      # Project configuration
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── apps/                       # Django applications
│   ├── __init__.py
│   └── tasks/                  # Tasks app
│       ├── __init__.py
│       ├── admin.py            # Django admin configuration
│       ├── apps.py             # App configuration
│       ├── models.py           # Database models
│       ├── serializers.py      # DRF serializers
│       ├── views.py            # API views
│       ├── urls.py             # App URL patterns
│       ├── tests.py            # Unit tests
│       └── migrations/         # Database migrations
│
├── docs/                       # Documentation
│   └── swagger/
│       └── tasks_schemas.py    # Swagger schema definitions
│
└── utils/                      # Utility modules
    └── response.py             # Custom response utilities
```

## 🛠️ Technology Stack

- **Backend**: Django 5.2.1
- **API Framework**: Django REST Framework
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Database**: SQLite (development), PostgreSQL (production)
- **Configuration**: python-decouple
- **Python**: 3.12+

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd django_rest_api_project
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (PostgreSQL - Optional)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Database Setup
```bash
# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

## 🔗 API Endpoints

### Base URL: `http://127.0.0.1:8000/api/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/{id}/` | Get a specific task |
| PUT | `/api/tasks/{id}/` | Update a specific task |
| DELETE | `/api/tasks/{id}/` | Delete a specific task |

### Task Model Structure
```json
{
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "completed": false,
    "created_at": "2025-10-04T12:00:00Z",
    "updated_at": "2025-10-04T12:00:00Z"
}
```

## 📖 API Usage Examples

### 1. Get All Tasks
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/
```

### 2. Create a New Task
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
-H "Content-Type: application/json" \
-d '{
    "title": "New Task",
    "description": "Task description",
    "completed": false
}'
```

### 3. Get Specific Task
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/1/
```

### 4. Update Task
```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
-H "Content-Type: application/json" \
-d '{
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
}'
```

### 5. Delete Task
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/
```

## 📚 API Documentation

### Swagger UI
Interactive API documentation is available at:
- **Swagger**: http://127.0.0.1:8000/swagger/
- **ReDoc**: http://127.0.0.1:8000/redoc/

### Django Admin
Access Django admin panel at:
- **Admin**: http://127.0.0.1:8000/admin/

## 🏗️ Architecture Explanation

### 1. **Models** (`apps/tasks/models.py`)
- Defines the database structure for tasks
- Uses Django ORM for database interactions
- Includes validation and constraints

### 2. **Serializers** (`apps/tasks/serializers.py`)
- Handles data serialization/deserialization
- Validates incoming data
- Converts Python objects to JSON and vice versa

### 3. **Views** (`apps/tasks/views.py`)
- Contains the business logic
- Handles HTTP requests and responses
- Uses Django REST Framework's APIView class

### 4. **URLs** (`apps/tasks/urls.py` & `config/urls.py`)
- Maps URLs to view functions
- Defines API endpoints structure

### 5. **Settings** (`config/settings.py`)
- Central configuration file
- Database, middleware, and app settings
- Environment-based configuration

## 🔧 Development Workflow

### 1. Making Changes to Models
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 2. Adding New Features
1. Update models if needed
2. Create/update serializers
3. Implement views
4. Add URL patterns
5. Update Swagger documentation
6. Write tests

### 3. Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.tasks
```

## 🚀 Deployment

### Environment Variables for Production
```env
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
SECRET_KEY=your-production-secret-key

# PostgreSQL for production
DB_NAME=production_db
DB_USER=production_user
DB_PASSWORD=secure_password
DB_HOST=your-db-host
DB_PORT=5432
```

### Database Migration to PostgreSQL
1. Install PostgreSQL
2. Update `.env` with PostgreSQL credentials
3. Update `settings.py` to use PostgreSQL configuration
4. Run migrations: `python manage.py migrate`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running (if using PostgreSQL)
   - Check database credentials in `.env`
   - Switch to SQLite for development

2. **Migration Issues**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Import Errors**
   - Ensure virtual environment is activated
   - Install dependencies: `pip install -r requirements.txt`

4. **Port Already in Use**
   ```bash
   # Use different port
   python manage.py runserver 8001
   ```

## 📞 Support

For questions or issues, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed description

---

**Happy Coding! 🎉**