from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 25116728
api_hash = "8fef459b63e30e0d4c7febd57d036648"
phone = "+994707909293"

# The channel/Group name that you want to get messages from
source_channel_name = 'main bitches'

# The channel/Group that you want to send messages to
destination_channel_link = -1002037183141

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code:'))

async def send_to_destination(message, channel):
    await client.send_message(entity=channel, message=message)

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title == source_channel_name:
            # Check if the word "profit" is in the message
            if "profit" in event.message.text.lower():
                # Forward the message as is to the destination channel
                await send_to_destination(event.message.text, destination_channel_link)

    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit

client.start()
client.run_until_disconnected()
