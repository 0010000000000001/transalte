#   many more ideas for code optimization, but everything has its time.

import random
import requests
import os
from time import sleep
from colorama import Fore, Back, init
import subprocess
import webbrowser
from API import api, trs, url

init()

__author__ = '0010000000000001'

#   API
URL = url
TRANSlATE = trs
KEY = api

#   generator ru
list_ru = [f'{Fore.MAGENTA} Что ты хочешь а? O.o{Fore.RESET}', f'{Fore.MAGENTA} Что ты пытаешься сделать? (*_*){Fore.RESET}',
           f'{Fore.MAGENTA} Может что то другое выберешь? :3{Fore.RESET}',
           f'{Fore.MAGENTA} Наверное, лучше этого не делать, м?{Fore.RESET}',
           f'{Fore.MAGENTA} Опять что то не то! (>_<){Fore.RESET}']
unique_ru = set(list_ru)
random.shuffle(list_ru)

#   generator eng
list_eng = [f'{Fore.MAGENTA} What do you want? o.O{Fore.RESET}', f'{Fore.MAGENTA} What are you trying to do? (*_*){Fore.RESET}',
            f'{Fore.MAGENTA} Maybe something else? :3{Fore.RESET}', f'{Fore.MAGENTA} Probably best not, eh? (>_<){Fore.RESET}',
            f'{Fore.MAGENTA} Difficult to understand &_&{Fore.RESET}']
unique_eng = set(list_eng)
random.shuffle(list_eng)


def menu():
    counter = 1
    language = '''
    1.English scoreboard\n
    2.Deutsch - Ru\n
    3.Greek - Ru\n
    4.Ukrainian scoreboard\n
    5.Spanish - Ru\n
    6.Latin - Ru\n
    7.Russian scoreboard\n
    8.French - Ru\n
    9.Italian - Ru\n
    10.Chinese - Ru
                        '''

    from_eng = '''
        1. Eng - Russian\n
        2. Eng - Ukrainian
                        '''

    from_ukr = '''
        1. Ukr - English\n
        2. Ukr - Russian
                            '''

    from_ru = '''
        1. Ru - English\n
        2. Ru - Deutsch\n
        3. Ru - Greek\n
        4. Ru - Ukrainian\n
        5. Ru - Spanish\n
        6. Ru - French\n
        7. Ru - Italian\n
        8. Ru - Kazakh\n
        9. Ru - Chinese\n
                        '''

    while True:
        print('\n 1.Language menu \n 2.Open github url')
        choice = input('\n Choose a number: ')

        if choice == '1':
            os.system('MODE CON COLS=71 LINES=23')
            print(language)
            headers = {'Authorization': f'Basic {KEY}'}
            auth = requests.post(url=URL, headers=headers)
            token = auth.text

            if auth.status_code == 200:
                while True:
                    selection = input(f"{Fore.CYAN}  To exit to the main menu, write:{Fore.RED} exit"
                                      F'\n{Fore.RESET}  Language for translation: ')

                    if selection == 'exit':
                        os.system('cls')
                        break
                        print(language)

                    elif selection == '1':  # from eng
                        print(from_eng)
                        on = True
                        while on:
                            number = input('  Language selection: ')
                            if number == 'exit':
                                print(language)
                                break

                            if number == '1':   # eng menu
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_eng)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1033, 'dstLang': 1049}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '2':   # eng - ukr
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_eng)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(
                                            f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                            f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1033, 'dstLang': 1058}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                    elif selection == '2':  # de
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1031, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    elif selection == '3':  # greek
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1032, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    elif selection == '4':  # ukr menu
                        print(from_ukr)
                        on = True
                        while on:
                            number = input(' Language selection: ')
                            if number == 'exit':
                                print(language)
                                break

                            if number == '1':   # ukr - eng
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ukr)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1058, 'dstLang': 1033}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '2':   # ukr - ru
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ukr)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1058, 'dstLang': 1049}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                    elif selection == '5':  # es - ru
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1034, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    elif selection == '6':  # la - ru
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1142, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    elif selection == '7':  # ru menu
                        print(from_ru)
                        on = True
                        while on:
                            number = input(' Language selection: ')
                            if number == 'exit':
                                print(language)
                                break

                            if number == '1':   # ru - eng
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1033}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '2':   # ru - de
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1031}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '3':   # ru - gr
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1032}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '4':   # ru - ukr
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1058}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '5':   # ru - span
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1034}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '6':   # ru - fr
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1036}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '7':   # ru - it
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break

                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1040}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '8':   # ru - kz
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1087}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                            if number == '9':   # ru - chi
                                while True:
                                    words = input(f"\n{Fore.RESET} Enter a word: ")
                                    if words == 'exit':
                                        print(from_ru)
                                        break
                                    while words in ('2', '4') or len(words) == 1:
                                        print('  -' * 8)
                                        print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                        print('  -' * 8)
                                        words = input(f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                                      f"\n{Fore.RESET} Enter a word: ")

                                    headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                                    params = {'text': words, 'srcLang': 1049, 'dstLang': 1028}
                                    r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                                    res = r.json()

                                    try:
                                        print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                        print('-' * 37)

                                    except:
                                        print('  -' * 8)
                                        try:
                                            print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                            print('  -' * 8)

                                        except:
                                            print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                            print('  -' * 8)

                    elif selection == '8':      # fr to ru
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1036, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    elif selection == '9':      # ital to ru
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1040, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    elif selection == '10':      # chi to ru
                        while True:
                            words = input(f"\n{Fore.RESET} Enter a word: ")
                            if words == 'exit':
                                print(language)
                                break
                            while words in ('2', '4') or len(words) == 1:
                                print('  -' * 8)
                                print(f'{Fore.MAGENTA} Better give me a word!{Fore.RESET}')
                                print('  -' * 8)
                                words = input(
                                    f"\n{Fore.CYAN}To exit to the main menu, write:{Fore.RED} exit"
                                    f"\n{Fore.RESET} Enter a word: ")

                            headers_translate = {'Authorization': 'Bearer ' f'{token}'}
                            params = {'text': words, 'srcLang': 1028, 'dstLang': 1049}
                            r = requests.get(url=TRANSlATE, headers=headers_translate, params=params)
                            res = r.json()

                            try:
                                print(f"{Fore.YELLOW}\nTranslation:{Fore.RESET}", res['Translation']['Translation'])
                                print('-' * 37)

                            except:
                                print('  -' * 8)
                                try:
                                    print(list_eng.pop(random.randint(0, len(list_eng) - 1)))
                                    print('  -' * 8)

                                except:
                                    print(f"{Fore.RED} I can not find..{Fore.RESET}")
                                    print('  -' * 8)

                    else:
                        print('  -' * 8)
                        print(f"{Fore.RED} Сhoose the correct option!{Fore.RESET}")
                        print('  -' * 8)

            elif auth.status_code == 400 or 401:
                print(f"{Fore.RED}Unable to connect to the server, connection attempt after 2 minutes..{Fore.RESET}")
                sleep(2)

        elif choice == '2' and counter == 1:
            print(f' {Back.CYAN}{Fore.BLACK}The link was opened in your browser.{Fore.RESET}{Back.RESET}')
            sleep(1)
            webbrowser.open('https://github.com/0010000000000001/transalte.git', new=0)
            counter += 1

        elif choice == '2' and counter == 2:
            response = None
            while response not in ('y', 'n'):
                response = input(f'\n{Fore.CYAN} - Reopen the link? y/n: {Fore.RESET}').lower()

            if response == 'y':
                print(f' {Back.CYAN}{Fore.BLACK}The link was opened in your browser again.{Fore.RESET}{Back.RESET}')
                sleep(1)
                webbrowser.open('https://github.com/0010000000000001/transalte.git', new=0)

            elif response == 'n':
                print(f' {Back.CYAN}{Fore.BLACK}Link will not open{Back.RESET}{Fore.RESET}')
                sleep(1)
                os.system('cls')

        else:
            print('  -' * 8)
            print(f"{Fore.RED} Сhoose the correct option!{Fore.RESET}")
            print('  -' * 8)


def main():
    os.system('MODE CON COLS=71 LINES=20')
    print(f"{Fore.YELLOW}\n To connect a translator, you need to check your internet connection..{Fore.BLACK}")
    internet = False
    print(f'\n {Fore.BLACK}{Back.YELLOW}flashing indicator counts seconds{Back.RESET}')
    print(f' {Fore.RESET}please dont interrupt:{Back.RESET}{Fore.BLACK}')
    while not internet:
        try:
            subprocess.check_call(["ping", "www.google.com"])
            os.system("cls")
            internet = True
            print(f'{Fore.RESET} Dictionary for quick translation from the DESKTOP')
            print(f' | • {Fore.CYAN}github.com/0010000000000001 {Fore.RESET}|')
            sleep(2)
            print(f"\n {Fore.YELLOW}Successfully, your internet is working!{Fore.RESET}")
            menu()

        except subprocess.CalledProcessError:
            print(f"{Fore.RED} There is no internet connection, connection attempt..{Fore.RESET}{Fore.BLACK}")
            sleep(10)


if __name__ == '__main__':
    main()
    sleep(6)
