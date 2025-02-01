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

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(128), nullable=False)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    second_name: Mapped[str] = mapped_column(String(64), nullable=True)
    display_name: Mapped[str] = mapped_column(String(128), nullable=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    profile_photo: Mapped[str] = mapped_column(String(256), nullable=False)
    profile_photo_preview: Mapped[str] = mapped_column(String(256), nullable=False)
    background_photo: Mapped[str] = mapped_column(String(256), nullable=False)
    about: Mapped[str] = mapped_column(Text, nullable=True)
    phone: Mapped[str] = mapped_column(String(16), nullable=True)
    city: Mapped[str] = mapped_column(String(64), nullable=True)
    birthday: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    is_confirmed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_2fa_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    otp: Mapped["TwoFactorAuthentication"] = relationship("TwoFactorAuthentification", backref="User")
    servers: Mapped[List["Server"]] = relationship("Server", backref="User", secondary="ServerUser", )


class TwoFactorAuthentication(Base):
    __tablename__ = "TwoFactorAuthentication"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    secret_key: Mapped[str] = mapped_column(String(512), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False)


class Session(Base):
    __tablename__ = "Session"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hash: Mapped[str] = mapped_column(String(256), nullable=False)
    expires: Mapped[int] = mapped_column(Integer, nullable=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete='CASCADE'), nullable=True)


class Server(Base):
    __tablename__ = "Server"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    photo_url: Mapped[str] = mapped_column(String(512), nullable=True)
    users: Mapped[List["User"]] = relationship("User",
                                               backref="Server",
                                               secondary="ServerUser",
                                               order_by="User.id")
    role: Mapped[List["Role"]] = relationship("Role", backref="Server")
    category: Mapped["Category"] = relationship("Category", backref="Server")
    channel: Mapped[List["Channel"]] = relationship("Channel", backref="Server")


class ServerUser(Base):
    __tablename__ = "ServerUser"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete='CASCADE'), nullable=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("Server.id", ondelete='CASCADE'), nullable=True)


class Category(Base):
    __tablename__ = "Category"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    server_id: Mapped[str] = mapped_column(ForeignKey("Server.id", ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    channels: Mapped[List["Channel"]] = relationship("Channel", backref="Category", order_by="Channel.id")


class Channel(Base):
    __tablename__ = "Channel"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("Server.id", ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    type_id: Mapped[int] = mapped_column(ForeignKey("Type.id", ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    type: Mapped["Type"] = relationship("Type", backref="Channel")
    server: Mapped["Server"] = relationship("Server", backref="Channel")
    messages: Mapped[List["Message"]] = relationship("Message", backref="Channel")
    role: Mapped[List["Role"]] = relationship("Role", backref="Channel")


class Type(Base):
    __tablename__ = "Type"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Role(Base):
    __tablename__ = "Role"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    color: Mapped[str] = mapped_column(String(7), nullable=False, default="#FFFFFF")
    is_displayable: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    is_taggable: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("Server.id"), nullable=False)
    server: Mapped["Server"] = relationship("Server", backref="Role")
    permissions: Mapped[List["Permission"]] = relationship("Permission", backref="Role", order_by="Permission.id")
    users: Mapped[List["User"]] = relationship("User", backref="Role", secondary="RoleUser")


class RoleUser(Base):
    __tablename__ = "RoleUser"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete='CASCADE'), nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("Role.id", ondelete='CASCADE'), nullable=True)


class Permission(Base):
    __tablename__ = "Permission"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("Role.id", ondelete='CASCADE'), nullable=False)
    role: Mapped["Role"] = relationship("Role", backref="Permission")
    can_view_channels: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_edit_channels: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_edit_roles: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_view_journal: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_moderate_server: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_create_invites: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_edit_nickname: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_moderate_nickname: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_kick_user: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_ban_user: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_timeout_user: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_send_message: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_create_channels: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_attach: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_reacting: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_moderate_message: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_connect: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_speak: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_use_webcam: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_mute_users: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_disable_earphones_users: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    can_manipulate_users_voice: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)


class Message(Base):
    __tablename__ = "Message"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    edit_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_edited: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id", ondelete='SET NULL'), nullable=True)
    server_id: Mapped[int] = mapped_column(ForeignKey("Server.id", ondelete='CASCADE'), nullable=False)
    server: Mapped["Server"] = relationship("Server", backref="Message")
    from_user: Mapped["User"] = relationship("User", backref="Message")
    attachments: Mapped[List["Attachment"]] = relationship("Attachment", backref="Message")


class Attachment(Base):
    __tablename__ = "Attachment"

    serialize_only = ()

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    url: Mapped[str] = mapped_column(String(512), nullable=False)
    message_id: Mapped[int] = mapped_column(ForeignKey("Message.id", ondelete='CASCADE'), nullable=False)
    message: Mapped["Message"] = relationship("Message", backref="Attachment")

