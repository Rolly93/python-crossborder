import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a 2-second network delay
    print("Data fetched!")
    return {"result": "some data"}

async def process_data(data):
    print("Processing data:", data)
    await asyncio.sleep(1)
    print("Data processed!")

async def main():
    print("Starting...")
    data = await fetch_data()  # Pause main() until fetch_data() completes
    await process_data(data)  # Pause main() until process_data() completes
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())