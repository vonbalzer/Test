import requests




def creat_folder(def_token_ya, folder):
    url_yandex_disk_creat_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Connect-type': 'application/json', 'Authorization': f'{def_token_ya}'}
    params = {"path": {folder}}
    res_ya = requests.put(url_yandex_disk_creat_folder, headers=headers, params=params)

    if '409' in str(res_ya) or '201' in str(res_ya):
        return f'Создана папка с именем на YandexDisk: {folder}'
    elif '401' in str(res_ya):
        return f'Указанный вами токен YandexDisk неверный' \
               f' или не предоставляет достаточных прав для заливки фотографий.'
    else:
        return f'Ошибка: {str(res_ya)} ==> {res_ya.json()["message"]}'


