from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CreateDTO
from sqlmodel import select
from .router import router
from uuid import UUID
from fastapi import (
    Depends, 
    status, 
    HTTPException, 
    Response
)


@router.delete('/{coleta_id}', status_code.HTTP_204_NO_COMTEMD)
async def delete(coleta_id: UUID, db: AsyncSession = Depend(get_session)):
    async with db as session:
        query = select(CreateDTO).filter(CreateDTO.id == coleta_id)
        result = await session.execute(query)
        coleta_del: CreateDTO = result.scalar_one_or_none()

        if coleta_del:
            await session.delete(coleta_del)
            await session.commit()

            return Response(
                status_code=status.HTTP._204_NO_CONTEND)      
        
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='ID Não encontrado!'
            )