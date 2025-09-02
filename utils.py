
import asyncio
from typing import AsyncGenerator

def diff(old: str, new: str) -> str:
    if not old:
        return f"New data: {new}"
    if old == new:
        return "No changes since last request."
    return f"Previous: {old}\nNow: {new}"

async def stream_text(text: str) -> AsyncGenerator[str, None]:
    for word in text.split():
        yield word + " "
        await asyncio.sleep(0.1)