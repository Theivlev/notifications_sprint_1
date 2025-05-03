from typing import List, Tuple
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from src.service.notifications import get_notifications_service, NotificationsService
from src.paginations.pagination import PaginationLimits
from src.shemas.notifications_history import NotificationRecordResponse
from src.shemas.delivery import DeliveryDTO

router = APIRouter()


@router.get(
    "/",
    summary="Получение истории уведомлений",
    description="Возвращает список уведомлений пользователя с учетом пагинации.",
    response_model=List[NotificationRecordResponse]
)
async def get_history(
    user_id: str,
    pagination: Tuple[int, int] = Depends(PaginationLimits.get_pagination_params),
    service: NotificationsService = Depends(get_notifications_service),
):
    try:
        uuid_obj = UUID(user_id)
        filter_ = {"user_id": uuid_obj}
        page_number, page_size = pagination
        history_records = await service.get_history(filter_, page_number, page_size)
        return [NotificationRecordResponse.from_history(record) for record in history_records]

    except HTTPException as e:
        raise e
    except ValueError:
        raise HTTPException(status_code=400, detail="Некорректный формат user_id. Ожидается UUID.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.post(
    "/",
    summary='Уведомление пользователей',
    description='Отправка уведомление пользователям',
    response_model=dict,
)
async def notification(
    delivery_data: DeliveryDTO,
    service: NotificationsService = Depends(get_notifications_service),
):
    try:
        await service.notification(delivery_data)
        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )