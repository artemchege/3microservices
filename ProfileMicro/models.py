from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    city = Column(String)

    subscriptions = relationship('Subscription', back_populates='user_profile')

    def __repr__(self):
        return f'Profile obj with id: {self.id}'


class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created = Column(DateTime(timezone=True), onupdate=func.now())
    name = Column(String, primary_key=True, index=True)

    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    user_profile = relationship('Profile', back_populates='subscriptions', lazy='subquery')

    def __repr__(self):
        return f'Subscription obj with id: {self.id}'
