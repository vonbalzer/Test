
from bokin import secretary_program_start
from yandex import creat_folder

if __name__ == '__main__':
   token_ya = 'AQAAAABWJXu6AADLWxMjEvsREEV6voCafcSxa-Q'
   name = 'Folder'
   secretary_program_start()
   print(creat_folder(token_ya, name))
