import pandastable
import requests
import fake_useragent
import pandas
import tkinter
import time
import graphic_data


user_agent = fake_useragent.UserAgent()
keyword = '廚具'
name = []
historical_sold = []
price = []
number_of_transactions = 500  #須為100的倍數
def add_data(url):
    req = requests.get(url, headers={ 'user-agent': user_agent.random })
    # print(req.text)
    data = req.json()
    data2 = data["items"]
    # print(data2)
    for i in range(len(data2)):
        name.append(data2[i]['item_basic']['name'])
        historical_sold.append(data2[i]['item_basic']['historical_sold'])
        price.append(data2[i]['item_basic']['price'] / 100000)
    # print(name)

def show_GUI_table(df):
    app = tkinter.Tk()
    app.geometry('600x400+200+100')
    app.title('商品列表')
    f = tkinter.Frame(app)
    f.pack(fill=tkinter.BOTH, expand=1)

    table = pt = pandastable.Table(f, dataframe=df,
                                   showtoolbar=True, showstatusbar=True)
    pt.show()
    app.mainloop()


def create_df():
    for i in range(0, number_of_transactions, 100):
        url = 'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword='+keyword+'&limit='+str(100)+'&newest='+str(i)+'&order=desc&page_type=search&version=2'
        print(url)
        add_data(url)
        time.sleep(1)
    df = pandas.DataFrame({
        '商品名稱': name,
        '已售出數量': historical_sold,
        '價格': price,
    })
    return df


