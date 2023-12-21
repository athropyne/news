from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import CursorResult, select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncConnection
from starlette import status
from starlette.responses import JSONResponse

from database import get_connection
from exc import NewsNotFound
from models import NewNewsModel, NewNewsContainer, UpdateNewsModel, NewsAliases
from schemas import news

router = APIRouter()


@router.post("/")
async def new(
        model: NewNewsModel,
        connection: AsyncConnection = Depends(get_connection)
):
    container = NewNewsContainer(
        **model.model_dump(by_alias=True),
    )

    cursor: CursorResult = await connection.execute(
        insert(news).values(**container.model_dump(by_alias=True)).returning(news)
    )
    result = dict(cursor.mappings().one())
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(result)
    )


@router.put("/{ID}")
async def update(
        ID: UUID,
        model: UpdateNewsModel,
        connection: AsyncConnection = Depends(get_connection)
):
    cursor: CursorResult = await connection.execute(
        news.update().values(**model.model_dump(by_alias=True)).where(news.c[NewsAliases.ID] == ID).returning(news)
    )
    if cursor.rowcount == 0:
        raise NewsNotFound
    result = dict(cursor.mappings().one())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )


@router.get("/list")
async def get_list(
        skip: int = 0,
        limit: int = 30,
        connection: AsyncConnection = Depends(get_connection)
):
    fields = [column for column in news.columns if column.name != NewsAliases.CONTENT]
    print(fields)
    cursor: CursorResult = await connection.execute(
        select(*fields).offset(skip).limit(limit)
    )
    result = cursor.mappings().fetchall()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )


@router.get("/{ID}")
async def get_by_id(
        ID: UUID,
        connection: AsyncConnection = Depends(get_connection)
):
    cursor: CursorResult = await connection.execute(
        select(news).where(news.c[NewsAliases.ID] == ID)
    )
    result = cursor.mappings().one_or_none()
    if result is None:
        raise NewsNotFound
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(dict(result))
    )


@router.delete("/{ID}")
async def delete(
        ID: UUID,
        connection: AsyncConnection = Depends(get_connection)
):
    cursor: CursorResult = await connection.execute(
        news.delete().where(news.c[NewsAliases.ID] == ID)
    )
    if cursor.rowcount == 0:
        raise NewsNotFound
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content="новость удалена"
    )
