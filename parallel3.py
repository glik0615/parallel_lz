import asyncio
async def message():
    for i in range(5):
        print(f"{i + 1}")
        await asyncio.sleep(1)
async def main():
    await message()

asyncio.run(main())
asyncio.run(message())