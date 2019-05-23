import csv
import urllib.request as req
from bs4 import BeautifulSoup

urls = {
'KEB하나':'https://www.mibank.me/exchange/bank/index.php?search_code=005',
'우리은행':'https://www.mibank.me/exchange/bank/index.php?search_code=020',
'국민은행':'https://www.mibank.me/exchange/bank/index.php?search_code=004',
'신한은행':'https://www.mibank.me/exchange/bank/index.php?search_code=088',
'NH농협':'https://www.mibank.me/exchange/bank/index.php?search_code=011',
'IBK기업은행':'https://www.mibank.me/exchange/bank/index.php?search_code=003',
'SC제일은행':'https://www.mibank.me/exchange/bank/index.php?search_code=023',
'씨티은행':'https://www.mibank.me/exchange/bank/index.php?search_code=027',
'Sh수협은행':'https://www.mibank.me/exchange/bank/index.php?search_code=007',
'부산은행':'https://www.mibank.me/exchange/bank/index.php?search_code=032',
'DGB대구은행':'https://www.mibank.me/exchange/bank/index.php?search_code=031',
'전북은행':'https://www.mibank.me/exchange/bank/index.php?search_code=037',
'경남은행':'https://www.mibank.me/exchange/bank/index.php?search_code=039',
'제주은행':'https://www.mibank.me/exchange/bank/index.php?search_code=035'
}

country_list = []

def load(urls):
    exchangeDB={}
    for key, value in urls.items():
        bank = req.urlopen(value).read()
        date = BeautifulSoup(bank,'html.parser').find('h5', class_="update").get_text().replace('\n','').replace('\t','')
        soup = BeautifulSoup(bank,'html.parser').find('tbody')
        country = soup.find_all('td', class_="first")
        cash = soup.find_all('td', class_="right")
        check1, check2, currency_data = [], [], {}
        for i in country:
            check1.append(i.get_text())
        for i in cash:
            check2.append(i.get_text())
        n = 0
        for i in check1:
            currency_data[i]=check2[n:n+7]
            n += 7
        exchangeDB[key]=date,currency_data
    return exchangeDB

# print(load(urls))

def loadDB():
    db = load(urls)
    tmp_dict = {}
    for key0, value0 in db.items():
        for key1, value1 in value0[1].items():
            if key1 in tmp_dict:
                # print(tmp_dict[key1])
                if type(tmp_dict[key1]) == list:
                    tmp_dict[key1].append([key0, value1[0], value0[0]])
                else:
                    tmp_dict[key1] = [tmp_dict[key1], [key0 ,value1[0], value0[0]]]
            else:
                tmp_dict[key1] = [[key0, value1[0], value0[0]]]

    return tmp_dict
# print(loadDB())

# dictionary -> data files, 국가목록 생성
def create_data():
    data = loadDB()
    country_list = []
    for country, dd in data.items():
        with open('data/'+country, 'wt', encoding='UTF8') as f:
            f.write("은행,환율,업데이트시간\n")
            for i in dd:
                if i[1] == '-':
                    pass
                else:
                    i = str(i).replace("[","").replace("]","").replace("'","")
                    f.write("%s\n"%(i))
        country_list.append(country)

    with open('data/country_list', 'wt', encoding='UTF8') as l:
        for x in country_list:
            l.write("%s\n"%(x))
