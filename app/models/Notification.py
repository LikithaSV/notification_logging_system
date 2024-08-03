from tortoise import Model, fields

class Notification(Model):
    id = fields.IntField(primary_key=True)
    communication_id = fields.CharField(max_length=50,unique=True)
    sender = fields.CharField(max_length=50)
    receiver = fields.CharField(max_length=50)
    type = fields.CharField(max_length=10)
    status_code = fields.IntField(default=200)
    status = fields.CharField(max_length=50)
    time_stamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "notifications"
    
    def to_dict(self):
        return {
            "id":self.id,
            "communication_id":self.communication_id,
            "sender":self.sender,
            "receiver":self.receiver,
            "type":self.type,
            "status_code":self.status_code,
            "status":self.status,
            "time_stamp":str(self.time_stamp)
        }