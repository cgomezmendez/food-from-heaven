from twilio.rest import Client
from ffh.util.localization import _

account_sid = 'AC74574c0777a0a37539d9148377ad57da'

auth_token = '6236880e8387b4f77d67b0b42e94ba09'

client = Client(account_sid, auth_token)

daily_dish_message_template = _('Good morning, {}.\nToday we have {}.\nWould you like to order?')

message = client.messages.create(
        to='whatsapp:+18298679985',
        from_='whatsapp:+14155238886',
        body=daily_dish_message_template.format('Jesus', 'Arroz, habichuelas, chuletas ahumadas, ensaladas y frituras'));

print(message.sid)
