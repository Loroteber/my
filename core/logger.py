from colorama import Fore, Back, Style, init
init(autoreset=True)

def log(name, text, msg_type="msg"):
    colors = {
        "msg": Fore.WHITE,
        "succ": Fore.GREEN,
        "warn": Fore.YELLOW,
        "err": Fore.RED
    }

    color = colors.get(msg_type, Fore.WHITE)

    print(f'[{name}] {color}{text}')