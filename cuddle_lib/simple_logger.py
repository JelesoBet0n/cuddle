import time
from colorama import Fore

date = time.strftime('%H%M%S-%d%b%y')
directory = f"logs/log{date}.txt"


class SimpleLogger:
    @staticmethod
    def request(text):
        print(f"{Fore.LIGHTBLUE_EX}REQUEST: {Fore.LIGHTWHITE_EX}{text}\n{Fore.WHITE}{time.strftime('%H:%M:%S, %D')}")
        with open(f"{directory}", "a") as logger:
            part = f"SERVER: {text}     -{time.strftime('%H:%M:%S, %D')}\n"
            logger.write(part)

    @staticmethod
    def responce(text):
        print(f"    {Fore.LIGHTBLUE_EX}RESPONCE: {Fore.LIGHTWHITE_EX}{text}\n"
              f"    {Fore.WHITE}{time.strftime('%H:%M:%S, %D')}")
        with open(f"{directory}", "a") as logger:
            part = f"SERVER: {text}     -{time.strftime('%H:%M:%S, %D')}\n"
            logger.write(part)

    @staticmethod
    def server(text):
        print(f"{Fore.LIGHTRED_EX}SERVER: {Fore.LIGHTWHITE_EX}{text}\n"
              f"{Fore.WHITE}{time.strftime('%H:%M:%S, %D')}")
        with open(f"{directory}", "a") as logger:
            part = f"SERVER: {text}     -{time.strftime('%H:%M:%S, %D')}\n"
            logger.write(part)
