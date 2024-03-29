from datetime import datetime
from pprint import pprint

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///example2.db")
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # dummy_field = Column(String)

    def __repr__(self):
        return f'id: {self.id}  username: {self.username}  ' \
               f'is_staff: {self.is_staff}  created at: {self.created_at}'


if __name__ == "__main__":
    Base.metadata.create_all()
    user_tolyan = User(username='tol1', is_staff=True)
    # user_tolyan.write()
    pprint(user_tolyan)
