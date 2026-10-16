from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.session import get_db
from app.schema.common.country import GetCountry
from app.schema.common.state import GetState
from app.model import Country, State

app = FastAPI()

@app.get("/country", response_model=list[GetCountry])
def get_countries(db: Session = Depends(get_db)) -> list[GetCountry]:

    statement = select(Country)
    countries = db.scalars(statement).all()
    return countries

@app.get("/state", response_model=list[GetState])
def get_states(db: Session = Depends(get_db)) -> list[GetState]:

    statement = select(State)
    states = db.scalars(statement).all()
    return states