from app import app
from src.event import models


@app.get('/events/{event_id}', response_model=models.Event)
async def get_event(event_id: int):
    return models.Event.query.get(id=event_id)