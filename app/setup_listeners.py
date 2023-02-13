from app.constants import ListenerEventTypes


## this should be moved from here to listeners folder.
async def notify_server_started_after_five_seconds(app, loop):
    pass

## this should only be present in this file.
listeners = [
    (
        notify_server_started_after_five_seconds,
        ListenerEventTypes.AFTER_SERVER_START.value,
    )
]
