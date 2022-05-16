import os
from icrawler.builtin import GoogleImageCrawler


# Функция которая принимает запрос, и создает по нему название папки
def input_request():
    fold_name = ''
    req_text = input(f"Введите запрос: ")
    for i in req_text:
        if i.isalnum():
            fold_name += i

    if fold_name == '':  # Если введенный запрос будет только из символов, создадим папку со своим названием
        fold_name = "Папка под картинки"
    return req_text, fold_name


# Создаю директорию, проверяя есть ли она
def create_folder(fold_name):
    if not os.path.isdir(f"{fold_name}"):
        os.mkdir(f"{fold_name}")


request_text, folder_name = input_request()
print(request_text, folder_name)

create_folder(folder_name)

num_pic = 15

google = GoogleImageCrawler(storage={'root_dir': f'{folder_name}'})
google.crawl(keyword=request_text, max_num=num_pic)
