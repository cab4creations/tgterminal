import asyncio
from pyrogram import Client
from pyrogram.enums import ChatAction


def select_chat_action() -> ChatAction:
    print("Please, select chat action:")

    for i, action in enumerate(ChatAction):
        print(f"{i + 1}) {action.name}")

    chat_actions_count = len(ChatAction.__members__)

    while True:
        try:
            action_number = int(input(f"Enter value (1-{chat_actions_count}): "))
            return  list(ChatAction.__members__.values())[action_number - 1]
        except (ValueError, IndexError):
            print("[Invalid value]")


async def send_infinity_chat_actions(
    app: Client, chat_id: int, chat_action: ChatAction
) -> None:
    while True:
        await app.send_chat_action(chat_id=chat_id, action=chat_action)
        await asyncio.sleep(5)
