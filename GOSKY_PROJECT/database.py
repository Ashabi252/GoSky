from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_connection_URL =  "mysql+pymysql://root:Asha%40252@localhost:3306/gosky_db"


engine = create_engine(db_connection_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


