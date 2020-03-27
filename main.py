import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    vk_session = vk_api.VkApi(
        token='7216621803de07eafa776329fb518f1eeb5f5764fae3c32e24769bb3dd76d2817b50403d52a1dbf217f69')

    longpoll = VkBotLongPoll(vk_session, 193461113)
    user_id = None

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            text = event.obj.message['text'].lower()
            if text == 'привет' or text == 'здравствуйте':
                reply = 'И вам не хворать'
            elif text == 'тест':
                reply = 'хорош меня тестить!'
            else:
                reply = 'Сейчас отвечу, если не сплю'
            vk = vk_session.get_api()
            user_id = event.obj.message['from_id']

            vk.messages.send(user_id=user_id,
                             message=reply,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
