import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "Data fetched"

async def main():
    data = await fetch_data()
    print(data)

if __name__ == "__main__":
    asyncio.run(main())