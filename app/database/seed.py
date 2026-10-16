from app.core.utils import read_json_file
from sqlalchemy.orm import Session
from sqlalchemy import select
from .session import SessionLocal
from app.model import Country, State, Currency

countries_file_path = "data/countries.json"
states_file_path = "data/states.json"
currencies_file_path = "data/currencies.json"

def seed_countries(db: Session, countries: list[dict]) -> None:

    for country in countries:
        statement = select(Country).where(Country.code==country.get("iso3"))
        exist = db.scalars(statement).first()
        if not exist:
            country_data = {
                "id": country.get("id"),
                "code": country.get("iso3"),
                "country": country.get("name")
            }
            db.add(Country(**country_data))

    db.commit()

def seed_states(db: Session, states: list[dict]) -> None:

    for state in states:
        statement = select(State).where(State.country_id==state.get("country_id"), State.state==state.get("name"))
        exist = db.scalars(statement).first()
        if not exist:
            state_data = {
                "state": state.get("name"),
                "country_id": state.get("country_id")
            }
            db.add(State(**state_data))

    db.commit()

def seed_currencies(db: Session, currencies: list[dict]) -> None:

    for currency in currencies:
        statement = select(Currency).where(Currency.currency==currency.get("currency") and Currency.code==currency.get("code"))
        exist = db.scalars(statement).first()
        if not exist:
            currency = Currency(**currency)
            db.add(currency)

    db.commit()
def run_seed():

    db = SessionLocal()
    try:
        print("start seeding...")
        countries = read_json_file(countries_file_path)
        seed_countries(db, countries)
        states = read_json_file(states_file_path)
        seed_states(db, states)
        currencies = read_json_file(currencies_file_path)
        seed_currencies(db, currencies)
        print("seeding done")
    finally:
        db.close()

if __name__ == "__main__":

    run_seed()