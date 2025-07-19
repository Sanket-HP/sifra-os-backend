from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Command(BaseModel):
    text: str

@router.post("/")
async def speak(command: Command):
    return {"response": f"Sifra heard: {command.text}"}
