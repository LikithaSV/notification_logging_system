from app.repositories.notificaton_repo import NotificationRepo

class NotificationManager:
    @classmethod
    async def create_notification(cls,payload):
        response = await NotificationRepo.create_notification(payload)
        return response