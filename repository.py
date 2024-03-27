from sqlalchemy import select

from database import new_session, CardNumberOrm, WinnerOrm
from shemas import CardNumberInfo, Winner


class Repository:
    @classmethod
    async def add_card_number(cls, card_number_data: CardNumberInfo):
        async with new_session() as session:
            card_number_dict = card_number_data.model_dump()

            card_number = CardNumberOrm(**card_number_dict)
            session.add(card_number)
            await session.flush()
            await session.commit()
            return card_number.id

    @classmethod
    async def get_winners(cls) -> list[Winner]:
        async with new_session() as session:
            query = select(WinnerOrm)
            result = await session.execute(query)
            winner_models = result.scalars().all()
            winners = [Winner.model_validate(winner_model.__dict__) for winner_model in
                       winner_models]
            return winners
