from fastapi import APIRouter
from models.form_model import BogieChecksheetForm, WheelSpecificationForm
from app.data.store import wheel_forms, bogie_forms

router = APIRouter()

@router.post("/api/forms/wheel-specifications")
def submit_wheel_form(form: WheelSpecificationForm):
    wheel_forms.append(form)
    return {
        "message": "Wheel specification submitted successfully",
        "data": form
    }

@router.post("/api/forms/bogie-checksheet")
def submit_bogie_form(form: BogieChecksheetForm):
    bogie_forms.append(form)
    return {
        "message": "Bogie form submitted successfully",
        "data": form
    }
