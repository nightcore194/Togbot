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
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    second_name: Mapped[str] = mapped_column(String(64), nullable=True)
    display_name: Mapped[str] = mapped_column(String(128), nullable=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    profile_photo_url: Mapped[str] = mapped_column(String(256), nullable=False)
    background_photo_url: Mapped[str] = mapped_column(String(256), nullable=False)
    about_user: Mapped[str] = mapped_column(Text, nullable=True)
    phone: Mapped[str] = mapped_column(String(16), nullable=True)
    city: Mapped[str] = mapped_column(String(64), nullable=True)
    birthday: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    is_confirmed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class Session(Base):
    __tablename__ = "Session"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hash: Mapped[str] = mapped_column(String(256), nullable=False)
    expires: Mapped[int] = mapped_column(Integer, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=True)



class Server(Base):
    __tablename__ = "Server"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Category(Base):
    __tablename__ = "Category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Channel(Base):
    __tablename__ = "Channel"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Role(Base):
    __tablename__ = "Role"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Permission(Base):
    __tablename__ = "Permission"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Message(Base):
    __tablename__ = "Message"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Attachment(Base):
    __tablename__ = "Attachment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class EmojiPack(Base):
    __tablename__ = "EmojiPack"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class EmojiObject(Base):
    __tablename__ = "EmojiObject"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
