from ffh.util.models import Base, User
from ffh.util.db import engine

Base.metadata.create_all(engine)
