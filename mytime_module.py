import asyncio
from userbot.events import register
from datetime import datetime
from pytz import timezone

@register(outgoing=True, pattern="^.time")
async def time(e):
	tz = timezone("Asia/Irkutsk")
	hour = str(datetime.now(tz).hour)
	minute = str(datetime.now(tz).minute)
	if len(hour) < 2:
		hour = "0"+hour
	if len(minute) < 2:
		hour = "0"+minute
	text = f"У меня {hour}:{minute}"
	await e.edit(text)