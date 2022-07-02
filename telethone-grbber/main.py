import configparser
import json

from telethon.sync import TelegramClient
# from telethon import connection
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('anon',api_id,api_hash)


async def dump_all_prtis(channel):
    off_setuser = 0
    limit_user = 100

    all_participants = []
    filter_user = ChannelParticipantsSearch('')
    i = 0
    while i<100:
        participants = await client(GetParticipantsRequest(channel,
			filter_user, off_setuser, limit_user, hash=0))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        off_setuser += len(participants.users)
        i+=1

    all_user_id = []

    for i in all_participants:
        if i.username =='None':
            pass
        else:
            all_user_id.append(i.username)

    with open('id_user.json','w',encoding='utf8') as file:
        json.dump(all_user_id,file,ensure_ascii=False)


async def main():
    url = input('Введите ссылку на канал или чат')
    channel = await client.get_entity(url)
    await dump_all_prtis(channel)


with client:
    client.loop.run_until_complete(main())