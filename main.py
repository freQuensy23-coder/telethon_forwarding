from telethon import TelegramClient, events
from config import api_id, api_hash
from MemList import MemoryList

INPUT_CHANNELS = MemoryList(name="INPUT_CHANNELS")
OUTPUT_CHANNEL = 'resend_channel'


client = TelegramClient('resend_bot', api_id, api_hash)


@client.on(events.NewMessage(chats=INPUT_CHANNELS))
async def normal_handler(event):
    if event.message.text.find("/add") != -1:
        INPUT_CHANNELS.append(event.message.text.removeprefix("/add").strip())
        return None
    await client.send_message(OUTPUT_CHANNEL, event.message)

client.start()
client.run_until_disconnected()
