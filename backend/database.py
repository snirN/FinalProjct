from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

URL_DATABASE = os.getenv("URL_DATABASE")

engine = create_engine(URL_DATABASE,echo=True)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()