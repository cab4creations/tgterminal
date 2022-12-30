from pydantic import BaseModel, validator
from pyrogram.enums import ChatType


class TgChat(BaseModel):
    id: int
    first_name: str | None
    last_name: str | None
    title: str | None
    type: ChatType

    @validator("type", pre=True)
    def handle_chat_type(cls, value):
        if type(value) is ChatType:
            return value

        return ChatType.__members__[value.upper()]

    @property
    def name(self) -> str:
        if self.first_name and self.last_name:
            name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            name = self.first_name
        else:
            name = self.title

        return name

    @property
    def data(self) -> dict:
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            title=self.title,
            type=self.type.name,
        )
        
    def __str__(self):
        return f"{self.name} (id={self.id})"
