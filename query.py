import requests
from bs4 import BeautifulSoup
import re

class query:
    def __init__(self):
        self.reslist = []

    def openFile(self , fileName):
        with open(fileName , 'r' , encoding='utf8') as f:
            while True:
                line = f.readline().strip('\n')
                if not line :
                    break
                zip_code = self.query(line)
        
                if not zip_code == None:
                    res = '%s\t%s' % (zip_code , line)
                    self.reslist.append(res)

    def query(self , addr):
        url = 'http://tools.5432.tw/zip5?adrs=' + addr
        res = requests.get(url)
        soup = BeautifulSoup(res.text , 'html.parser')
        r = soup.find('div' , class_ = 'zip5-result-result')
        key_word = re.compile('[0-9]+')
        try:
            return key_word.findall(str(r))[1]
        except:
            return 'Something error'

    def writeFile(self , fileName):
        with open(fileName , 'w' , encoding='utf8') as f:
            newlist = [str(i) +'\n' for i in self.reslist]
            f.writelines(newlist)


def main():
    a = query()
    a.openFile('addr.txt')
    a.writeFile('result.txt')

if __name__ == '__main__':
    main()








