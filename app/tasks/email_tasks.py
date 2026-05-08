from app.celery_worker import celery_app
import time

@celery_app.task
def send_email():
    print("Starting email process...")
    
    time.sleep(10)

    print("Email sent successfully")

    return "SUCCESS"
