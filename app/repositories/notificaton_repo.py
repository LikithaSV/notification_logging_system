from tortoise_wrapper.wrappers.db_wrapper import ORMWrapper
from app.models.Notification import Notification

class NotificationRepo:
    @classmethod
    async def create_notification(cls,payload):
        communication_id = payload.get("communication_id")
        sender = payload.get("sender")
        receiver = payload.get("receiver")
        type = payload.get("type")
        status_code = payload.get("status_code")
        status = payload.get("status")
        time_stamp = payload.get("time_stamp")

        try:
            notification = await ORMWrapper.create(model=Notification,payload={
                "communication_id":communication_id,
                "sender":sender,
                "receiver":receiver,
                "type":type,
                "status_code":status_code,
                "status":status
            })
            return {"success":True,"notification":notification.to_dict()}
        except Exception as e:
            print(str(e))
            return {"success":False,"error":str(e)}