import os
from webwhatsapi import WhatsAPIDriver
from ffh.util import menu, redis
import datetime
from loguru import logger

logger.info('Starting daily dish reminder task')

redis_instance = redis.get_redis()
current_date = datetime.datetime.now()

daily_dish_time_str = '08:00'

comida_del_cielo_id = '18296490148-1543101812@g.us'
test_group_id = '18298679985-1551975140@g.us'

daily_dish_time = datetime\
    .datetime.combine(current_date,
                      datetime.datetime.strptime(
                          daily_dish_time_str, '%H:%M')
                      .time())

date_format = '%d_%m_%Y'

daily_dish_reminder_key = 'DAILY_DISH_REMINDER_' + \
    current_date.strftime(date_format)

ran_today = redis_instance.get(daily_dish_reminder_key)

if ran_today:
    logger.info('Stopping daily dish reminder task - Already sent')
    exit()

if (daily_dish_time - current_date) > datetime.timedelta(minutes=30):
    logger.info('Stopping daily dish reminder task - Time hasn\'t arrive')
    exit()

menu_items = menu.get_menu()


today_dish = menu_items.get(datetime.date.today())

if not today_dish:
    logger.info('Stopping daily dish reminder task - No dish for today')
    exit()

logger.info('Daily dish reminder - Dish found, sending message')

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSc6kSPKeZNvGsRXuowis8xvDRTuaGEPDYFI9mehp3GWALLbTg/viewform'

today_dish_message = 'Buenos dias chicos, para hoy:\n{}\nPorfavor recuerden llenar el formulario.\n{}\nEnviado desde un bot en pruebas, reportar cualquier error.'.format(
    today_dish, form_url)


profiledir = os.path.join(".", "firefox_cache")
if not os.path.exists(profiledir):
    os.makedirs(profiledir)

try:
    driver = WhatsAPIDriver(username='tester', loadstyles=False,
                            client='remote',
                            command_executor='http://localhost:4444/wd/hub',
                            profile=profiledir)

#qr = driver.get_qr()
# print(qr)
    # driver.wait_for_login()
# driver.save_firefox_profile(remove_old=False)
#    chats = driver.get_all_chats()
    #chats = driver.get_all_chats()
    # print(chats)
    driver.send_message_to_id(
        comida_del_cielo_id, today_dish_message)
    redis_instance.set(daily_dish_reminder_key, 'True')
    logger.info('Ending Daily dish reminder - Message Sent')

except Exception as ex:
    logger.error(ex)
    driver.quit()
