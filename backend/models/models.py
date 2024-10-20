import datetime
from flask_login import UserMixin

from sqlalchemy import String, Integer, ForeignKey, Text, Date, Boolean, DateTime, ARRAY, func
from sqlalchemy.event import listens_for
from sqlalchemy.orm import mapped_column, Mapped, relationship, DeclarativeBase
from sqlalchemy_serializer import SerializerMixin

from typing import List


class Base(DeclarativeBase, SerializerMixin):
    pass


class User(Base, UserMixin):
    __tablename__ = "User"


class Session(Base):
    __tablename__ = "Session"


class Server(Base):
    __tablename__ = "Server"


class Category(Base):
    __tablename__ = "Category"


class Channel(Base):
    __tablename__ = "Channel"


class Role(Base):
    __tablename__ = "Role"


class Permission(Base):
    __tablename__ = "Permission"


class Message(Base):
    __tablename__ = "Message"


class Attachment(Base):
    __tablename__ = "Attachment"


class EmojiPack(Base):
    __tablename__ = "EmojiPack"


class EmojiObject(Base):
    __tablename__ = "EmojiObject"
