import asyncio


# Define coroutine that simulates a time-consuming task
# async def fetch_data(delay):
#     print("fetching data ....")
#     await asyncio.sleep(delay)
#     print("Data fetched successfully")
#     return {"data": "Some data"}
#
# # coroutine function
# async def main():
#     print("Starting of the main coroutine")
#     task = fetch_data(2)
#     # Await the fetch_data coroutine, pausing the execution of the main until the fetch_data completes
#     result = await task
#     print(f"Received result: {result}")
#     print("End of the main coroutine")
#
# #Run the main coroutine
# asyncio.run(main())


# 
# async def fetch_data(delay, id):
#     print("Fetching data.. id:", id)
#     await asyncio.sleep(delay)
#     print("Data fetched, id:", id)
#     return {"data": "Some data", "id": id}
# 
# 
# async def main():
#     result = await asyncio.gather(fetch_data(1, 2), fetch_data(1, 3), fetch_data(1, 4))
#     print(result)
# 
# asyncio.run(main())


async def fetch_data(delay, id):
    print("Fetching data.. id:", id)
    await asyncio.sleep(delay)
    return {"data": "Some data", "id": id}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, delay))
            tasks.append(task)

        # After the Task Group block, all tasks have completed
        results  = [task.result() for task in tasks]

        for result in results:
            print(f"Received result: {result}")



asyncio.run(main())