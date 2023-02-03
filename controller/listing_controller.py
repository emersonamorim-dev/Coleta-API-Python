from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CreateDTO
from sqlmodel import select
from fastapi import Depends
from .router import router
from typing import List

@router.get('/', response_model=List[CreateDTO])
async def listing(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CreateDTO)
        result = await session.execute(query)
        courses: List[CreateDTO] = result.scalrs().all()

        return courses