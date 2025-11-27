import os
import getpass # to get system username for fastapi since devenv sets user to local user
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine

from typing import Annotated

# Database
db_user = os.getenv("PGSUSER", getpass.getuser())
db_password = os.getenv("PGSPASSWORD", "")
db_host = os.getenv("PGHOST", "localhost")
db_port = os.getenv("PGPORT", "5432")
db_name = os.getenv("PGDATABASE", "ascs_db")

if db_host.startswith("/"):
    postgresql_url = f"postgresql://{db_user}:{db_password}@/{db_name}?host={db_host}"
else:
    postgresql_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

connect_args ={}
engine = create_engine(postgresql_url, echo=True) #FIXME: remove echo=True, it's only on for learning purposes

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
# initial endpoints
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

