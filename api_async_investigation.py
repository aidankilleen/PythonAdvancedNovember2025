# api_async_investigation.py

import asyncio
import time
import httpx

from tqdm.asyncio import tqdm

async def fetch(client, url):
    response = await client.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

async def progress():
    for i in range(50):
        print (f"\u2588", end="", flush=True)
        await asyncio.sleep(0.25)

async def tqdm_progress(seconds):
    with tqdm(total=seconds, desc="Downloading...", unit="s") as pbar:
        for i in range(seconds):
            await asyncio.sleep(1)
            pbar.update(1)

async def main():
    async with httpx.AsyncClient() as client:
        
        t1 = asyncio.create_task(fetch(client, "https://api.acodingtutor.com/members/1?_delay=5000"))
        t2 = asyncio.create_task(fetch(client, "https://api.acodingtutor.com/members/8?_delay=7000"))
        t3 = asyncio.create_task(tqdm_progress(7))
        r1, r2, _ = await asyncio.gather(t1, t2, t3)
        print (r1)
        print (r2)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print ()
print (f"time taken: {end_time - start_time}")
print ("Finished")
