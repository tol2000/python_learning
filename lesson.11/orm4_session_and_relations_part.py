from datetime import datetime
from pprint import pprint

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///example2.db")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


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

    with Session() as session:
        user_tolyan = User(username='tol1', is_staff=True)
        session.add(user_tolyan)
        pprint(user_tolyan)
        session.commit()
        pprint(user_tolyan)
