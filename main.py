import asyncio
from pyrogram import Client

import config
from app.select_chat import select_chat
from app.chat_action import select_chat_action, send_infinity_chat_actions


async def main():
    app = Client(
        "va_acc1",
        config.API_ID,
        config.API_HASH,
        app_version="Telegram Desktop 4.1.1 x64",
        device_model="intel",
    )
    await app.start()

    print("TgTerminal successfully started.")

    while True:
        print("What do you want to do?")
        print("1) Send infinitely chat actions.")

        action_number = input(f"Enter value: ").strip()

        match action_number:
            case "1":
                chat = await select_chat(app)
                chat_action = select_chat_action()

                print(
                    f'Sending infinitely chat actions "{chat_action.name}" to chat {chat}...'
                )

                await send_infinity_chat_actions(app, chat.id, chat_action)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nClosing TgTerminal. Goodbey!")
