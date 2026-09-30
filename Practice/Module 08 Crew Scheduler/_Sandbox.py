from datetime import datetime
from dataclasses import dataclass
from typing import Any
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel



class CreateBookingRequest(BaseModel):
    start_date: str
    end_date: str
    project_name: str


@dataclass
class Result:
    success: bool
    status: str
    details: dict[str, Any] | None = None 


class BookCrewMember:
    def __init__(self, crew_db: dict) -> None:
        self.crew_db = crew_db

    def exec(self, person_name: str, start_date: str, end_date: str, project_name: str) -> Result:
        if person_name not in self.crew_db: 
            return Result(False, "person_not_found")

        required_start = datetime.strptime(start_date, "%Y-%m-%d").date()
        required_end = datetime.strptime(end_date, "%Y-%m-%d").date()

        for booking in self.crew_db[person_name]["bookings"]:
            booking_start = datetime.strptime(booking["start"], "%Y-%m-%d").date()
            booking_end = datetime.strptime(booking["end"], "%Y-%m-%d").date()

            if required_start <= booking_end and required_end >=booking_start:
                return Result(False, "dates_overlap", {"req_dates": [required_start, required_end], 
                                                       "busy_dates": f"{booking_start} - {booking_end}",})
        new_booking = {
            "project": project_name,
            "start": start_date,
            "end": end_date
        }
        self.crew_db[person_name]["bookings"].append(new_booking)
        return Result(True, "success")


app = FastAPI()

@app.post("/crew/{person_name}/bookings")
def book_crew_route(person_name: str, body: CreateBookingRequest):

    result = book_crew_member.exec(
        person_name=person_name,
        start_date=body.start_date,
        end_date=body.end_date,
        project_name=body.project_name
    )

    if result.status == "success":
        return JSONResponse(status_code=204, content=None)
    elif result.status == "dates_overlap":
        return JSONResponse(status_code=409, content={"error": "dates_overlap", "details": result.details})
    elif result.status == "person_not_found":
        return JSONResponse(status_code=404, content={"error": "person_not_found"})
    else:
        return JSONResponse(status_code=500, content="unexpected_error")



crew_database = {
    "John": {
        "role": "Gaffer",
        "bookings": [
            {"project": "Movie A", "start": "2026-10-01", "end": "2026-10-05"}
        ]
    },
    "Ben": {
        "role": "DOP",
        "bookings": [
            {"project": "Movie A", "start": "2026-10-01", "end": "2026-10-05"}
        ]
    }
}

book_crew_member = BookCrewMember(crew_database)

