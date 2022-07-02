import configparser
import asyncio
from telethon import TelegramClient
import json



config = configparser.ConfigParser()
config.read('config.ini')
api_id = 13518955
api_hash =  '714d5f36878befda1df16f410aa41bc2'


client = TelegramClient('anon',api_id,api_hash)


async def send_message():
    with open('id_user.json') as file:
        template = json.load(file)
    
    text = '''                                              ‼️ ВНИМАНИЕ ‼️
    Доброго времени суток администрация поискового бота Глаз Бога уведомляет, что в этой реплике ⚠️ @GodSeeAllbot ⚠️процент правильного пробива людей 86.4 % , но к слову сказать там подписка стоит дешевле.
    Пожалуйста не ведитесь, что там дешевле, 100% пробив вы найдете только у нас.✅ '''
    for value in template:
        try:
            id = '@'+value
            await client.send_message(id,text) 
            template.remove(value)
        except:
            await asyncio.sleep(100)

        
    
async def get():
    await asyncio.sleep(500)
     
        


async def main():
    await send_message()

while True:
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception as e:
        file = open('bag.txt', 'a+')
        bag = f'{e}'
        file.write('\n'+bag)
        file.close()   
