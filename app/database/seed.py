from app.core.utils import read_json_file
from sqlalchemy.orm import Session
from sqlalchemy import select
from .session import SessionLocal
from app.model import Country, State, Currency, Language, Profession, Category, SubCategory, Skill
from app.core.constants import (COUNTRIES_FILE_PATH, STATES_FILE_PATH, CURRENCIES_FILE_PATH,
                                LANGUAGES_FILE_PATH, PROFESSIONS_FILE_PATH, CATEGORIES_FILE_PATH,
                                SUB_CATEGORIES_FILE_PATH, SKILLS_FILE_PATH)

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
        statement = select(Currency).where(Currency.currency==currency.get("currency") or Currency.code==currency.get("code"))
        exist = db.scalars(statement).first()
        if not exist:
            currency = Currency(**currency)
            db.add(currency)

    db.commit()

def seed_languages(db: Session, languages: list[dict]) -> None:

    for language in languages:
        statement = select(Language).where(Language.code == language.get("code") or Language.language == language.get("name"))
        exist = db.scalars(statement).first()
        if not exist:
            language_data = {
                "code": language.get("code"),
                "language": language.get("name")
            }
            db.add(Language(**language_data))

    db.commit()

def seed_professions(db: Session, professions: dict) -> None:

    for profession in professions.get("professions"):
        statement = select(Profession).where(Profession.profession==profession)
        exist = db.scalars(statement).first()
        if not exist:
            profession_data = {
                "profession": profession
            }
            db.add(Profession(**profession_data))

    db.commit()

def seed_categories(db: Session, categories: list[dict]) -> None:

    for category in categories:
        statement = select(Category).where(Category.category==category.get("category"))
        exist = db.scalars(statement).first()
        if not exist:
            category = Category(**category)
            db.add(category)

    db.commit()

def seed_sub_categories(db: Session, sub_categories: list[dict]) -> None:

    for sub_category in sub_categories:
        statement = select(SubCategory).where(SubCategory.sub_category==sub_category.get("sub_category"))
        exist = db.scalars(statement).first()
        if not exist:
            sub_category = SubCategory(**sub_category)
            db.add(sub_category)

    db.commit()

def seed_skills(db: Session, skills: list[dict]) -> None:

    for skill in skills:
        statement = select(Skill).where(Skill.skill==skill.get("skill"))
        exist = db.scalars(statement).first()
        if not exist:
            skill = Skill(**skill)
            db.add(skill)

    db.commit()


def run_seed() -> None:

    db = SessionLocal()
    try:
        print("start seeding...")

        countries = read_json_file(COUNTRIES_FILE_PATH)
        seed_countries(db, countries)

        states = read_json_file(STATES_FILE_PATH)
        seed_states(db, states)

        currencies = read_json_file(CURRENCIES_FILE_PATH)
        seed_currencies(db, currencies)

        languages = read_json_file(LANGUAGES_FILE_PATH)
        seed_languages(db, languages)

        professions = read_json_file(PROFESSIONS_FILE_PATH)
        seed_professions(db, professions)

        categories = read_json_file(CATEGORIES_FILE_PATH)
        seed_categories(db, categories)

        sub_categories = read_json_file(SUB_CATEGORIES_FILE_PATH)
        seed_sub_categories(db, sub_categories)

        skills = read_json_file(SKILLS_FILE_PATH)
        seed_skills(db, skills)

        print("seeding done")
    finally:
        db.close()

if __name__ == "__main__":

    run_seed()