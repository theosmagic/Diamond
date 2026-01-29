from fastapi import APIRouter, Depends
from app import models, auth

router = APIRouter(prefix="/api/protected", tags=["protected"])


@router.get("/dashboard")
def dashboard(current_user: models.User = Depends(auth.get_current_active_user)):
    """Example protected route - dashboard"""
    return {
        "message": f"Welcome to your dashboard, {current_user.username}!",
        "user_id": current_user.id,
        "email": current_user.email
    }


@router.get("/profile")
def get_profile(current_user: models.User = Depends(auth.get_current_active_user)):
    """Get user profile - example protected route"""
    return {
        "username": current_user.username,
        "email": current_user.email,
        "is_active": current_user.is_active,
        "created_at": current_user.created_at
    }
