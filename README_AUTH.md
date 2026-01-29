# User Authentication System

A secure user authentication system built with FastAPI, featuring JWT tokens, password hashing, and a modern web interface.

## Features

- ✅ User registration with email and username
- ✅ Secure login with JWT tokens
- ✅ Password hashing with bcrypt
- ✅ Protected routes with authentication middleware
- ✅ User profile endpoint
- ✅ Modern, responsive web interface
- ✅ RESTful API design
- ✅ SQLite database (easily switchable to PostgreSQL/MySQL)

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables (Optional)

```bash
cp .env.example .env
# Edit .env and set your SECRET_KEY
```

### 3. Run the Server

```bash
python run.py
```

Or using uvicorn directly:

```bash
uvicorn app.main:app --reload
```

### 4. Access the Application

- Web Interface: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative API Docs: http://localhost:8000/redoc

## API Endpoints

### Authentication

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/x-www-form-urlencoded

username=johndoe&password=securepassword123
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Get Current User
```http
GET /api/auth/me
Authorization: Bearer <access_token>
```

### Protected Routes

To access protected routes, include the JWT token in the Authorization header:

```http
Authorization: Bearer <your_access_token>
```

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── database.py          # Database setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── auth.py              # Authentication utilities
│   └── routers/
│       ├── __init__.py
│       └── auth.py          # Authentication routes
├── requirements.txt
├── run.py                   # Server entry point
├── .env.example
└── README_AUTH.md
```

## Security Features

1. **Password Hashing**: Uses bcrypt for secure password storage
2. **JWT Tokens**: Secure token-based authentication
3. **Token Expiration**: Tokens expire after 30 minutes (configurable)
4. **CORS Protection**: Configurable CORS middleware
5. **Input Validation**: Pydantic schemas validate all inputs

## Configuration

### Environment Variables

- `DATABASE_URL`: Database connection string (default: `sqlite:///./app.db`)
- `SECRET_KEY`: Secret key for JWT signing (CHANGE IN PRODUCTION!)
- `HOST`: Server host (default: `0.0.0.0`)
- `PORT`: Server port (default: `8000`)

### Token Settings

Edit `app/auth.py` to customize:
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time (default: 30)
- `ALGORITHM`: JWT algorithm (default: HS256)

## Database

The application uses SQLite by default. The database file (`app.db`) is created automatically on first run.

To use PostgreSQL or MySQL:

1. Update `DATABASE_URL` in `.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. Install the appropriate driver:
   ```bash
   # For PostgreSQL
   pip install psycopg2-binary
   
   # For MySQL
   pip install pymysql
   ```

## Usage Examples

### Python Client

```python
import requests

# Register
response = requests.post("http://localhost:8000/api/auth/register", json={
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
})

# Login
response = requests.post(
    "http://localhost:8000/api/auth/login",
    data={"username": "testuser", "password": "testpass123"}
)
token = response.json()["access_token"]

# Access protected route
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("http://localhost:8000/api/auth/me", headers=headers)
user = response.json()
```

### cURL

```bash
# Register
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'

# Login
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpass123"

# Get user info (replace TOKEN with actual token)
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer TOKEN"
```

## Adding Protected Routes

To create a protected route, use the `get_current_active_user` dependency:

```python
from fastapi import APIRouter, Depends
from app import models, auth

router = APIRouter()

@router.get("/protected")
def protected_route(current_user: models.User = Depends(auth.get_current_active_user)):
    return {"message": f"Hello {current_user.username}!"}
```

## Production Deployment

### Security Checklist

- [ ] Change `SECRET_KEY` to a strong random string
- [ ] Use environment variables for all secrets
- [ ] Set up HTTPS/TLS
- [ ] Configure CORS to allow only trusted origins
- [ ] Use a production database (PostgreSQL recommended)
- [ ] Set up proper logging
- [ ] Configure rate limiting
- [ ] Use a reverse proxy (nginx, Traefik, etc.)

### Running with Gunicorn

```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Testing

Create a test file to verify the authentication:

```python
# test_auth.py
import requests

BASE_URL = "http://localhost:8000"

# Test registration
response = requests.post(f"{BASE_URL}/api/auth/register", json={
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
})
print("Registration:", response.status_code)

# Test login
response = requests.post(
    f"{BASE_URL}/api/auth/login",
    data={"username": "testuser", "password": "testpass123"}
)
token = response.json()["access_token"]
print("Login successful, token:", token[:50] + "...")

# Test protected route
response = requests.get(
    f"{BASE_URL}/api/auth/me",
    headers={"Authorization": f"Bearer {token}"}
)
print("User info:", response.json())
```

## Troubleshooting

### Database errors
- Ensure SQLite has write permissions in the directory
- Check `DATABASE_URL` is correct

### Authentication fails
- Verify `SECRET_KEY` is set
- Check token expiration time
- Ensure password is correct

### CORS errors
- Update `allow_origins` in `app/main.py` for your frontend domain

## License

MIT License
