import os
import getpass

from sqlmodel import SQLModel, Session, create_engine

# Define variables to handle the way devenv sets up postgres
# TODO: look into modifying how devenv spins up postgresql 
database_user = os.getenv("PGSUSER", getpass.getuser())
database_password = os.getenv("PGSPASSWORD", "")
database_host = os.getenv("PGHOST", "localhost")
database_port = os.getenv("PGPORT", "5432")
database_name = os.getenv("PGDATABASE", "ascs_db")

if database_host.startswith("/"):
    postgresql_url = f"postgresql://{database_user}:{database_password}@/{database_name}?host={database_host}"
else:
    postgresql_url = f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"

engine = create_engine(postgresql_url, echo=True) #NOTE: echo=True is only on for learning

def init_database():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
