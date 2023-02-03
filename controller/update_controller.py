from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CreateDTO
from sqlmodel import select
from .router import router
from uuid import UUID

@router.put('/{coleta_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CreateDTO)
async def atualizar(coleta_id:UUID, coleta_dto: CreateDTO, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CreateDTO).filter(CreateDTO.id == coleta_id)
        result = await session.execute(query)
        coleta: CreateDTO = result.scalar_one_or_none()

        if coleta:
            coleta.type = coleta_dto.type
            coleta.daily = coleta_dto.daily
            coleta.destiny = coleta_dto.destiny
            coleta.time = coleta_dto.time
            coleta.price = coleta_dto.price

            await session.commit()

            return coleta

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Id não encontrando!'
            )
