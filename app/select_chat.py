import asyncio
import json

from pyrogram import Client
from pyrogram.enums import ChatType

from app.models import TgChat
import config


def select_chat_type() -> ChatType:

    print("Please, select chat type:")
    print("1) PRIVATE")
    print("2) BOT")
    print("3) GROUP")
    print("4) SUPERGROUP")
    print("5) CHANNEL")

    while True:
        chat_type = input("Enter value (1-5): ").strip()

        match chat_type:
            case "1":
                return ChatType.PRIVATE
            case "2":
                return ChatType.BOT
            case "3":
                return ChatType.GROUP
            case "4":
                return ChatType.SUPERGROUP
            case "5":
                return ChatType.CHANNEL
            case _:
                print("[Invalid value]")


async def select_chat(app: Client):
    print("Getting chats...")

    chats = None

    try:
        with open(config.CHAT_DB) as file:
            chats = [TgChat(**c) for c in json.load(file)]
    except FileNotFoundError:
        ...

    if not chats:
        print("Local chat database is not found.")
        print("Downloading chats. This may take some time...")

        chats = []

        dialogs = app.get_dialogs()

        async for d in dialogs:
            chat = TgChat(
                id=d.chat.id,
                first_name=d.chat.first_name,
                last_name=d.chat.last_name,
                title=d.chat.title,
                type=d.chat.type,
            )
            chats.append(chat)
            await asyncio.sleep(0.1)

        dict_chats = [chat.data for chat in chats]

        with open(config.CHAT_DB, "w") as file:
            json.dump(dict_chats, file)

        print("Successfully donwloaded chats.")

    chat_type = select_chat_type()

    print("Please, select chat:")

    chats_with_type = []
    
    for i, chat in enumerate(chats):
        if chat.type == chat_type:
            chats_with_type.append(chat)
            print(f"{len(chats_with_type)}) {chat.name} (id={chat.id})")

    while True:
        try:
            chat_number = int(input(f"Enter value (1-{len(chats)}): "))
            return chats_with_type[chat_number - 1]
        except (ValueError, IndexError):
            print("[Invalid value]")
