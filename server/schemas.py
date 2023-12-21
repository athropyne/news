from sqlalchemy import Table, Column, UUID, String, DateTime, MetaData

from models import NewsAliases

metadata = MetaData()
news = Table(
    "новости",
    metadata,
    Column(NewsAliases.ID, UUID(as_uuid=True), primary_key=True, nullable=False),
    Column(NewsAliases.TITLE, String(100), nullable=False),
    Column(NewsAliases.CONTENT, String(1000), nullable=False),
    Column(NewsAliases.CREATED_AT, DateTime, nullable=False)
)
