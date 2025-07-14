from fastapi import APIRouter
from models.form_model import WheelSpecificationForm
from app.data.store import wheel_forms, bogie_forms
router = APIRouter()

@router.get("/api/forms/wheel-specifications")
def get_wheel_forms():
    return {
        "data": wheel_forms,
        "message": "Wheel specs fetched successfully.",
        "success": True
    }

@router.get("/api/forms/bogie-checksheet")
def get_bogie_forms():
    return {
        "data": bogie_forms,
        "message": "Bogie forms fetched successfully.",
        "success": True
    }

