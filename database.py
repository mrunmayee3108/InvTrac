# connect FastAPI to database.
# engine: “A permanent connection pipeline to the database”
# session: “A temporary conversation with the database”. we cant directly communicate with the database, comm via session.
# sessionmaker creates a session generator. session()->creates a new DB session.
# bind=engine This tells SQLAlchemy: “Every session created should use THIS engine (DB connection).”
# autocommit=False -> Changes are NOT saved automatically. You must explicitly write: db.commit()
# autoflush=False. SQLAlchemy will NOT auto-send queries. It waits until: db.commit()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:Msp%403108@localhost:5432/product_db"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
