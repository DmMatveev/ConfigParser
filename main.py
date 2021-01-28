import pandas as pd
import os
from bs4 import BeautifulSoup

# data = pd.read_("C:\\Users\\user\\Desktop\\ConfigParser\\SendMailService.exe.config", encoding='utf-8')


def change_parametrs(timerIntervalVerification: int, timerIntervalTU):
    '''Функция для задания параметров ожидания <add key="timerIntervalVerification" value="60000"/>
                                               <add key="timerIntervalTU" value="360000"/>
                                               '''


def open_to_list(file_link):
    file = str
    file_temp = open(file_link,encoding='utf-8',mode='r')
    file = file_temp.read()
    file_temp.close()
    return file


os.chdir("C:\\Users\\user\\Desktop\\ConfigParser")
print(os.getcwd())
a = open_to_list("C:\\Users\\user\\Desktop\\ConfigParser\\SendMailService.exe.config")
print(f"!!!{a}!!!")
