import command_system
import vkapi
import random

def cat():
   # Получаем случайную картинку из паблика
   attachment = vkapi.get_random_wall_picture(-32015300)
   message = 'Вот тебе котик :)\nВ следующий раз я пришлю другого котика.'
   return message, attachment

cat_command = command_system.Command()

cat_command.keys = ['котик', 'кошка', 'кот', 'котенок', 'котяра', 'cat']
cat_command.description = 'Пришлю картинку с котиком'
cat_command.process = cat





def get_random_wall_picture(group_id):
    max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment