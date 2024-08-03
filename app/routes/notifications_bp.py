from sanic import Blueprint, Request
from torpedo import send_response
from app.managers.notification_manager import NotificationManager

notifications_bp = Blueprint("notifications_bp",url_prefix="/notifications")

@notifications_bp.post("/")
async def create_post(request:Request):
    print(request.json)
    communication_id = request.json.get("communication_id")
    sender = request.json.get("sender")
    receiver = request.json.get("receiver")
    type = request.json.get("type")
    status_code = request.json.get("status_code")
    status = request.json.get("status")

    if not(communication_id and sender and receiver and type and status_code and status):
        return send_response(data={"error":"Pleae provide required fields."},status_code=400)
    
    try:
        response = await NotificationManager.create_notification({
            "communication_id":communication_id,
            "sender":sender,
            "receiver":receiver,
            "type":type,
            "status_code":status_code,
            "status":status
        })
        if response.get("success"):
            return send_response(data={"notification":response.get("notification")},status_code=201)
        return send_response(data={"error":"Some database error occured, please try again later"},status_code=500)
    except Exception:
        return send_response(data={"error":"Some unexcpected error."},status_code=500)