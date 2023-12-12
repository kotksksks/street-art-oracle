import os
import time
import random
import schedule
import threading
import pandas as pd

sent_images = {}


def clear_list():
    sent_images.clear()
    schedule.every().day.at('02:00').do(clear_list)
    while True:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=clear_list).start()


def write_in_file(message):
    user_id = message.from_user.id
    text = message.text
    df = pd.DataFrame({'User ID': [user_id], 'Message': [text]})
    with pd.ExcelWriter('chats.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
    return True


def send_photo(message):
    user_id = message.from_user.id
    all_images = os.listdir('img')
    if user_id not in sent_images:
        sent_images[user_id] = set()
    rand_image = random.choice(all_images)
    while rand_image in sent_images[user_id]:
        rand_image = random.choice(all_images)
    sent_images[user_id].add(rand_image)
    return f'img/{rand_image}'
