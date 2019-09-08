from logging.config import fileConfig
from os import environ

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv('.env')

config = context.config

fileConfig(config.config_file_name)

target_metadata = None

url = environ.get('SQLALCHEMY_DATABASE_URI')


def run_migrations_offline():
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
