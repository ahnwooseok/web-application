from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import select
from database.connection import get_session
from models.events import Event, EventUpdate
from typing import List



event_router = APIRouter(tags=["Events"]) # Metadata for Swagger UI

# Endpoint Function for Create-Event Request
@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message" : "Event created successfully"
    }


# Endpoint Function for Retrieve-All-Events Request
@event_router.get("/", response_model= List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event) # Generates SQL Statement
    events = session.exec(statement).all() # to Select All Event Data
    return events # Executes SQL Statement and Gets Al Results

# Endpoint Function for Retrieve-Event Request
@event_router.get("/{id]", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id) # Gets an Event Data with supplied id
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUNT,
        datail="Event with supplied ID does not exist"
    )

# Endpoint Function for Update-Event Request
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value) # Updates the Event Data
        session.add(event) # Adds Updated Event Data
        session.commit() # Commits
        session.refresh(event) # Refresh the Event Data
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUNT,
        datail="Event with supplied ID does not exist"
    )

# Endpoint Function for Delete-Event Request
@event_router.delete("/delete/{id}", response_model=Event)
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id) # Gets an Event Data with supplied id
    if event:
        session.delete(event)
        session.commit()
        return {
            "message": "Event deleted successfully."
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUNT,
        datail="Event with supplied ID does not exist"
    )