import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    favorites = relationship("Favorite", back_populates="user")


class Planet(Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

    favorites = relationship("Favorite", back_populates="planet")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)

    planet_id = Column(Integer, ForeignKey("planets.id"))
    planet = relationship("Planet", back_populates="characters")

    favorites = relationship("Favorite", back_populates="character")


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    planet_id = Column(Integer, ForeignKey("planets.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")


# Draw from SQLAlchemy base
render_er(Base, "diagram.png")


def to_dict(self):
    return {}
