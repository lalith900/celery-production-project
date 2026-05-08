from fastapi import FastAPI
from app.tasks.email_tasks import send_email

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Celery Production App Running"}

@app.get("/send-email")
def trigger_email():

    task = send_email.delay()

    return {
        "task_id": task.id,
        "status": "Task submitted successfully"
    }
