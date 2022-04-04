import random
import requests
import os
from dotenv import load_dotenv
from time import sleep
from colorama import Fore, init
import subprocess
import webbrowser


init()
load_dotenv()

#   API
URL = 'https://developers.lingvolive.com/api/v1.1/authenticate'
TRANSlATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = os.getenv('KEY')

#   generator ru
list_ru = [f'{Fore.MAGENTA} Что ты хочешь а? O.o{Fore.RESET}', f'{Fore.MAGENTA} Что ты пытаешься сделать? (*_*){Fore.RESET}',
           f'{Fore.MAGENTA} Может что то другое выберешь? :3{Fore.RESET}',
           f'{Fore.MAGENTA} Наверное, лучше этого не делать, а? (>_<){Fore.RESET}']
unique_ru = set(list_ru)
random.shuffle(list_ru)

#   generator eng
list_eng = [f'{Fore.MAGENTA} What do you want? o.O{Fore.RESET}', f'{Fore.MAGENTA} What are you trying to do? (*_*){Fore.RESET}',
            f'{Fore.MAGENTA} Maybe something else? :3{Fore.RESET}', f'{Fore.MAGENTA} Probably best not, eh? (>_<){Fore.RESET}']
unique_eng = set(list_eng)
random.shuffle(list_eng)


def english(words):
    headers = {'Authorization': f'Basic {KEY}'}
    auth = requests.post(url=URL, headers=headers)
    token = auth.text
    if auth.status_code == 200:
        headers_translate = {'Authorization': 'Bearer ' f'{token}'}
        params = {'text': words, 'srcLang': 1033, 'dstLang': 1049}
        r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
        res = r.json()

        try:
            print(f"{Fore.YELLOW}\nRussian translation:{Fore.RESET}", res['Translation']['Translation'])
            print('-' * 37)

        except:
            print('  -' * 8)
            try:
                print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                print('  -' * 8)

            except:
                print(f"{Fore.RED} I can not find..{Fore.RESET}")
                print('  -' * 8)

    elif auth.status_code == 400 or 401:
        print(f"{Fore.RED}Unable to connect to the server, try again later..{Fore.RESET}")
        sleep(30)


def russian(words):
    headers = {'Authorization': f'Basic {KEY}'}
    auth = requests.post(url=URL, headers=headers)
    token = auth.text
    if auth.status_code == 200:
        headers_translate = {'Authorization': 'Bearer ' f'{token}'}
        params = {'text': words, 'srcLang': 1049, 'dstLang': 1033}
        r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
        res = r.json()

        try:
            print(f"{Fore.YELLOW}\nEnglish translation:{Fore.RESET}", res['Translation']['Translation'])
            print('-' * 37)

        except:
            print('  -' * 8)
            try:
                print(list_ru.pop(random.randint(0, len(list_ru) - 1)))
                print('  -' * 8)

            except:
                print(f"{Fore.RED} Не получается найти..{Fore.RESET}")
                print('  -' * 8)

    elif auth.status_code == 400 or 401:
        print(f"{Fore.RED}В настоящее время сервер недоступен, попробуйте позднее..{Fore.RESET}")
        sleep(30)


def translate():
    while True:
        choice = input('\n 1.English - Russian\n 2.Русский - Английский\n Choose a number: ')

        if choice == '1':
            while True:
                words = input(f"\n{Fore.CYAN}To exit to the main menu, write: exit\n{Fore.RESET}Enter a word: ")
                if words == 'exit':
                    break
                while words in ('2', '4') or len(words) == 1:
                    print('  -' * 8)
                    print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                    print('  -' * 8)
                    words = input(f"\n{Fore.CYAN}To exit to the main menu, write: exit\n{Fore.RESET}Enter a word: ")
                english(words)

        elif choice == '2':
            while True:
                words = input(f"\n{Fore.CYAN}Для выхода в основное меню команда: exit\n{Fore.RESET}Введите слово: ")
                if words == 'exit':
                    break
                while words in ('2', '4') or len(words) == 1:
                    print('  -' * 8)
                    print(f'{Fore.MAGENTA} Лучше дай мне слово!{Fore.RESET}')
                    print('  -' * 8)
                    words = input(f"\n{Fore.CYAN}Для выхода в основное меню команда: exit\n{Fore.RESET}Введите слово: ")
                russian(words)

        elif choice == 'exit':
            print(f"\n{Fore.CYAN} The program will close after 3 seconds..{Fore.RESET}")
            break

        else:
            print('  -' * 8)
            print(f"{Fore.RED} Not found!{Fore.RESET}")
            print('  -' * 8)


def main():
    print(f"{Fore.YELLOW}\nTo connect a translator, you need to check your internet connection..{Fore.BLACK}")
    internet = False
    while not internet:
        try:
            subprocess.check_call(["ping", "www.google.com"])
            os.system("cls")
            internet = True
            print(f"{Fore.RESET}\n| • https://github.com/0010000000000001 |",
                  f"\n\n{Fore.YELLOW} Successfully, your internet is working!{Fore.RESET}")
            webbrowser.open('https://github.com/0010000000000001/transalte.git', new=1, autoraise=True)
            translate()

        except subprocess.CalledProcessError:
            print(f"{Fore.RED}There is no internet connection, please wait 10 sec..{Fore.RESET}")
            sleep(10)
            response = None
            while response not in ('y', 'n'):
                response = input(f"\nTry reload the connection? y/n: ").lower()
                print(f'{Fore.BLACK}')
            if response == 'y':
                pass
            elif response == 'n':
                print(f"\n{Fore.CYAN}The program will close after 3 seconds..{Fore.RESET}")
                break


if __name__ == '__main__':
    main()
    sleep(3)
