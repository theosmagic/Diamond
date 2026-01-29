from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.database import init_db
from app.routers import auth, protected
import os

app = FastAPI(
    title="User Authentication API",
    description="A secure user authentication system with JWT tokens",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(protected.router)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve a simple login page"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Authentication</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                padding: 40px;
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #333;
                margin-bottom: 10px;
                text-align: center;
            }
            .subtitle {
                color: #666;
                text-align: center;
                margin-bottom: 30px;
                font-size: 14px;
            }
            .tabs {
                display: flex;
                margin-bottom: 30px;
                border-bottom: 2px solid #eee;
            }
            .tab {
                flex: 1;
                padding: 10px;
                text-align: center;
                cursor: pointer;
                color: #666;
                border-bottom: 2px solid transparent;
                transition: all 0.3s;
            }
            .tab.active {
                color: #667eea;
                border-bottom-color: #667eea;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                color: #333;
                font-weight: 500;
                font-size: 14px;
            }
            input {
                width: 100%;
                padding: 12px;
                border: 2px solid #eee;
                border-radius: 8px;
                font-size: 14px;
                transition: border-color 0.3s;
            }
            input:focus {
                outline: none;
                border-color: #667eea;
            }
            button {
                width: 100%;
                padding: 12px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
            button:active {
                transform: translateY(0);
            }
            .message {
                margin-top: 20px;
                padding: 12px;
                border-radius: 8px;
                text-align: center;
                font-size: 14px;
                display: none;
            }
            .message.success {
                background: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            .message.error {
                background: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            .message.show {
                display: block;
            }
            .user-info {
                margin-top: 20px;
                padding: 15px;
                background: #f8f9fa;
                border-radius: 8px;
                display: none;
            }
            .user-info.show {
                display: block;
            }
            .user-info p {
                margin: 5px 0;
                font-size: 14px;
                color: #333;
            }
            .logout-btn {
                margin-top: 10px;
                background: #dc3545;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 User Authentication</h1>
            <p class="subtitle">Secure login and registration</p>
            
            <div class="tabs">
                <div class="tab active" onclick="switchTab('login')">Login</div>
                <div class="tab" onclick="switchTab('register')">Register</div>
            </div>
            
            <div id="loginForm">
                <form onsubmit="handleLogin(event)">
                    <div class="form-group">
                        <label for="loginUsername">Username</label>
                        <input type="text" id="loginUsername" required>
                    </div>
                    <div class="form-group">
                        <label for="loginPassword">Password</label>
                        <input type="password" id="loginPassword" required>
                    </div>
                    <button type="submit">Login</button>
                </form>
            </div>
            
            <div id="registerForm" style="display: none;">
                <form onsubmit="handleRegister(event)">
                    <div class="form-group">
                        <label for="registerUsername">Username</label>
                        <input type="text" id="registerUsername" required>
                    </div>
                    <div class="form-group">
                        <label for="registerEmail">Email</label>
                        <input type="email" id="registerEmail" required>
                    </div>
                    <div class="form-group">
                        <label for="registerPassword">Password</label>
                        <input type="password" id="registerPassword" required>
                    </div>
                    <button type="submit">Register</button>
                </form>
            </div>
            
            <div id="message" class="message"></div>
            <div id="userInfo" class="user-info"></div>
        </div>
        
        <script>
            let token = localStorage.getItem('token');
            
            function switchTab(tab) {
                if (tab === 'login') {
                    document.getElementById('loginForm').style.display = 'block';
                    document.getElementById('registerForm').style.display = 'none';
                    document.querySelectorAll('.tab')[0].classList.add('active');
                    document.querySelectorAll('.tab')[1].classList.remove('active');
                } else {
                    document.getElementById('loginForm').style.display = 'none';
                    document.getElementById('registerForm').style.display = 'block';
                    document.querySelectorAll('.tab')[0].classList.remove('active');
                    document.querySelectorAll('.tab')[1].classList.add('active');
                }
                hideMessage();
            }
            
            function showMessage(text, type) {
                const msg = document.getElementById('message');
                msg.textContent = text;
                msg.className = 'message ' + type + ' show';
                setTimeout(hideMessage, 5000);
            }
            
            function hideMessage() {
                document.getElementById('message').classList.remove('show');
            }
            
            async function handleLogin(event) {
                event.preventDefault();
                const username = document.getElementById('loginUsername').value;
                const password = document.getElementById('loginPassword').value;
                
                const formData = new FormData();
                formData.append('username', username);
                formData.append('password', password);
                
                try {
                    const response = await fetch('/api/auth/login', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        token = data.access_token;
                        localStorage.setItem('token', token);
                        showMessage('Login successful!', 'success');
                        loadUserInfo();
                    } else {
                        showMessage(data.detail || 'Login failed', 'error');
                    }
                } catch (error) {
                    showMessage('Network error: ' + error.message, 'error');
                }
            }
            
            async function handleRegister(event) {
                event.preventDefault();
                const username = document.getElementById('registerUsername').value;
                const email = document.getElementById('registerEmail').value;
                const password = document.getElementById('registerPassword').value;
                
                try {
                    const response = await fetch('/api/auth/register', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ username, email, password })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        showMessage('Registration successful! Please login.', 'success');
                        setTimeout(() => switchTab('login'), 2000);
                    } else {
                        showMessage(data.detail || 'Registration failed', 'error');
                    }
                } catch (error) {
                    showMessage('Network error: ' + error.message, 'error');
                }
            }
            
            async function loadUserInfo() {
                if (!token) return;
                
                try {
                    const response = await fetch('/api/auth/me', {
                        headers: {
                            'Authorization': 'Bearer ' + token
                        }
                    });
                    
                    if (response.ok) {
                        const user = await response.json();
                        const userInfo = document.getElementById('userInfo');
                        userInfo.innerHTML = `
                            <p><strong>Logged in as:</strong> ${user.username}</p>
                            <p><strong>Email:</strong> ${user.email}</p>
                            <p><strong>User ID:</strong> ${user.id}</p>
                            <button class="logout-btn" onclick="logout()">Logout</button>
                        `;
                        userInfo.classList.add('show');
                    } else {
                        localStorage.removeItem('token');
                        token = null;
                    }
                } catch (error) {
                    console.error('Error loading user info:', error);
                }
            }
            
            function logout() {
                localStorage.removeItem('token');
                token = null;
                document.getElementById('userInfo').classList.remove('show');
                showMessage('Logged out successfully', 'success');
            }
            
            // Load user info on page load if token exists
            if (token) {
                loadUserInfo();
            }
        </script>
    </body>
    </html>
    """


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "authentication-api"}
