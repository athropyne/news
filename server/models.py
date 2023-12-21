import dataclasses
from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from typing import Optional


@dataclasses.dataclass
class NewsAliases:
    ID = "идентификатор"
    TITLE = "заголовок"
    CONTENT = "содержание"
    CREATED_AT = "дата создания"


class NewNewsModel(BaseModel):
    title: str = Field(max_length=100, alias=NewsAliases.TITLE)
    content: str = Field(max_length=1000, alias=NewsAliases.CONTENT)


class NewNewsContainer(NewNewsModel):
    ID: UUID = Field(default_factory=uuid4, alias=NewsAliases.ID)
    created_at: datetime = Field(default_factory=datetime.utcnow, alias=NewsAliases.CREATED_AT)


class UpdateNewsModel(BaseModel):
    title: Optional[str] = Field(max_length=100, alias=NewsAliases.TITLE)
    content: Optional[str] = Field(max_length=1000, alias=NewsAliases.CONTENT)
