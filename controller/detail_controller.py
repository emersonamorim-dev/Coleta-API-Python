from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CreateDTO
from sqlmodel import select
from .router import router
from typing import List
from uuid import UUID


@router.get('/{coleta_id}', response_model=CreateDTO, status_code=status.HTTP_200_OK)
async def detail(coleta_id:UUID, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CreateDTO).filter(CreateDTO.id == coleta_id)
        result = await session.execute(query)
        coleta: CreateDTO = result.scalar_one_or_none()

        if coleta:
            return coleta
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Id não encontrando!'
            )