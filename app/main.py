from fastapi import FastAPI
from app.routes import form_create, form_list


app = FastAPI()

# include both rutes
app.include_router(form_create.router)
app.include_router(form_list.router)
