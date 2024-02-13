import asyncio


response = {1:2}

async def gen(event: asyncio.Event):
    
    await event.wait()

    print(response)

    return response


async def ping(event: asyncio.Event):
    await asyncio.sleep(5)
    global response
    response = {2: 1}
    event.set()


async def main():
    event = asyncio.Event()
    asyncio.create_task(gen(event))
    await asyncio.create_task(ping(event))

asyncio.run(main())