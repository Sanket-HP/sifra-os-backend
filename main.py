from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "SifraOS backend is live!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "SifraOS backend"}

@app.post("/speak")
async def speak_command(command: str):
    # AI logic here
    return {"response": f"Sifra heard: {command}"}

@app.get("/recommendations")
async def get_recommendations(user_id: str):
    # Return personalized suggestions
    return {"apps": ["Calendar", "Health", "Reminders"]}

@app.get("/profile/{user_id}")
async def get_profile(user_id: str):
    return {
        "user_id": user_id,
        "name": "Sanket",
        "preferences": {"theme": "dark", "language": "en"}
    }

@app.get("/calendar")
async def get_calendar_events():
    return {
        "events": [
            {"title": "Meeting", "time": "10:00 AM"},
            {"title": "Doctor Appointment", "time": "2:00 PM"}
        ]
    }

@app.post("/notify")
async def notify_user(message: str):
    # Send notification logic
    return {"status": "sent", "message": message}
