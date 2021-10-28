import databases
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

DATABASE_URL = 'postgresql://postgres:abc123@localhost:5432/users_benchmark'

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', UUID, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('email', sqlalchemy.String),
    sqlalchemy.Column('created', sqlalchemy.DateTime),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
