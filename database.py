from datetime import datetime

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

engine = create_async_engine('sqlite+aiosqlite:///promotions_database.db')
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class CardNumberOrm(Model):
    __tablename__ = 'card_numbers'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    card_number: Mapped[str]


class WinnerOrm(Model):
    __tablename__ = 'winners'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    card_number: Mapped[str]
    phone_number: Mapped[bool]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
