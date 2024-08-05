from app.repositories.sms import ActionRepo

class SmsManager:

    @classmethod
    async def create(cls, payload):
        try:
            await ActionRepo.create(payload)
        except Exception as e:
            raise Exception(f"Error Occured dutring Creation of sms entry in sms table: {e}")

    @classmethod
    async def get_sms_payload(cls, comm_id, data):
        return {
            "comm_id": comm_id,
           
            "body": data.get('body'),
            
        }

    @classmethod
    async def get_sms(cls):
        try:
            await ActionRepo.get_()
        except Exception as e:
            Exception(f"{e} error occured during fetching sms")