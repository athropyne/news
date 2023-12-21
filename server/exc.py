from fastapi import HTTPException
from starlette import status

NewsNotFound = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="новость не найдена"
        )
