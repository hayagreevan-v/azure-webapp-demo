from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Azure App Service!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/env")
def environment():
    return {"environment": os.getenv("WEBSITE_SITE_NAME", "local")}
