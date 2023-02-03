from sqlalchemy.ext.asyncio import AsyncSession
from models.dao import get_session
from models.dto import CreateDTO
from .router import router
from uuid import uuid4
from fastapi import (
    status,
    Depends
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CreateDTO)
async def create(coleta_DTO: CreateDTO, db: AsyncSession = Depends(get_session)):
    novo_coleta = CreateDTO(
        id=str(uuid4()),
        type=coleta_DTO.type, 
        daily=coleta_DTO.daily, 
        destiny=coleta_DTO.destiny,
        time_modelo=coleta_DTO.ano_time,
        price=coleta_DTO.price
    )
    db.add(novo_coleta)
    await db.commit()

    return novo_coleta

