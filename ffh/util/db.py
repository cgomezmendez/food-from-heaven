from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ffh.db', echo=True)
Session = sessionmaker(bind=engine)
