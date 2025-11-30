import os
import getpass

from sqlmodel import SQLModel, Session, create_engine

# Define variables to handle the way devenv sets up postgres
# TODO: look into modifying how devenv spins up postgresql 
db_user = os.getenv("PGSUSER", getpass.getuser())
db_password = os.getenv("PGSPASSWORD", "")
db_host = os.getenv("PGHOST", "localhost")
db_port = os.getenv("PGPORT", "5432")
db_name = os.getenv("PGDATABASE", "ascs_db")

if db_host.startswith("/"):
    postgresql_url = f"postgresql://{db_user}:{db_password}@/{db_name}?host={db_host}"
else:
    postgresql_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(postgresql_url, echo=True) #NOTE: echo=True is only on for learning

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
