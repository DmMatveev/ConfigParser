from bs4 import BeautifulSoup

with open("C:\\Users\\user\\Desktop\\ConfigParser\\SendMailService.exe.config") as fp:
    soup = BeautifulSoup(fp, 'xml.parser')

soup = BeautifulSoup("<html>a web page</html>", 'xml.parser')

f = 3