# coding:utf-8
import requests
import json
from lxml import etree


# 获得url内容
def get_url(url, max_repeat_num=3):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko'}
    repeat_num = 0  # 重新连接次数
    is_right = True
    while repeat_num < max_repeat_num:
        try:
            response = requests.get(url, headers=headers, timeout=20)
        except requests.ConnectionError:
            is_right = False
            print('获得页面出错,正在重试...')
            repeat_num += 1
            continue
        is_right = True
        break
    if is_right:
        return response.text
    else:
        print('请检查网络连接是否正常')
        return


def get_book_url(book, **kwargs):
    while 1:
        response = get_url("https://book.douban.com/j/subject_suggest?q=%s" % book)
        results = json.loads(response)
        if len(results) >= 1:
            return results[0]['url']
        if len(book) >= 10:
            book = book[:10]
        if len(book) > 2:
            book = book[:-1]
        else:
            break



def get_douban_rate(url):
    response = get_url(url)
    page = etree.HTML(response)
    rate = None
    try:
        rate = page.xpath('//div[@id="interest_sectl"]//strong')[0]
        rate = float(rate.text.strip())
    except:
        print("Parse rate error")
        pass
    return rate


if __name__ == "__main__":
    url = get_book_url("数学女孩2")
    book_rate = get_douban_rate(url)
    print(book_rate)
