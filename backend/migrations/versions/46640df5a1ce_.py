"""empty message

Revision ID: 46640df5a1ce
Revises: 
Create Date: 2024-10-29 16:42:28.773889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46640df5a1ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Server',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('photo_url', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('second_name', sa.String(length=64), nullable=True),
    sa.Column('display_name', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('profile_photo_url', sa.String(length=256), nullable=False),
    sa.Column('background_photo_url', sa.String(length=256), nullable=False),
    sa.Column('about_user', sa.Text(), nullable=True),
    sa.Column('phone', sa.String(length=16), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('is_confirmed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['Server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Channel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['Server.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['Type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Message',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('edit_date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('is_edited', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['Server.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.Column('is_displayable', sa.Boolean(), nullable=False),
    sa.Column('is_taggable', sa.Boolean(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['Server.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Server_User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['Server.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Session',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('hash', sa.String(length=256), nullable=False),
    sa.Column('expires', sa.Integer(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Attachment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('url', sa.String(length=512), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['Message.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('can_view_channels', sa.Boolean(), nullable=False),
    sa.Column('can_edit_channels', sa.Boolean(), nullable=False),
    sa.Column('can_edit_roles', sa.Boolean(), nullable=False),
    sa.Column('can_view_journal', sa.Boolean(), nullable=False),
    sa.Column('can_moderate_server', sa.Boolean(), nullable=False),
    sa.Column('can_create_invites', sa.Boolean(), nullable=False),
    sa.Column('can_edit_nickname', sa.Boolean(), nullable=False),
    sa.Column('can_moderate_nickname', sa.Boolean(), nullable=False),
    sa.Column('can_kick_user', sa.Boolean(), nullable=False),
    sa.Column('can_ban_user', sa.Boolean(), nullable=False),
    sa.Column('can_timeout_user', sa.Boolean(), nullable=False),
    sa.Column('can_send_message', sa.Boolean(), nullable=False),
    sa.Column('can_create_channels', sa.Boolean(), nullable=False),
    sa.Column('can_attach', sa.Boolean(), nullable=False),
    sa.Column('can_reacting', sa.Boolean(), nullable=False),
    sa.Column('can_moderate_message', sa.Boolean(), nullable=False),
    sa.Column('can_connect', sa.Boolean(), nullable=False),
    sa.Column('can_speak', sa.Boolean(), nullable=False),
    sa.Column('can_use_webcam', sa.Boolean(), nullable=False),
    sa.Column('can_mute_users', sa.Boolean(), nullable=False),
    sa.Column('can_disable_earphones_users', sa.Boolean(), nullable=False),
    sa.Column('can_manipulate_users_voice', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['Role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Role_User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['Role.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Role_User')
    op.drop_table('Permission')
    op.drop_table('Attachment')
    op.drop_table('Session')
    op.drop_table('Server_User')
    op.drop_table('Role')
    op.drop_table('Message')
    op.drop_table('Channel')
    op.drop_table('Category')
    op.drop_table('User')
    op.drop_table('Type')
    op.drop_table('Server')
    # ### end Alembic commands ###
