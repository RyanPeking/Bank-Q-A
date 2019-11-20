import requests

def get_html(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*'
    }
    res = requests.get(url=url, headers=headers).content
    html = res.decode('utf-8')
    return html

if __name__ == '__main__':
    # word = '什么是利润率'
    # url = 'https://baike.baidu.com/search/none?word=' + word + '&pn=0&rn=10&enc=utf8'
    url = 'https://baike.baidu.com/item/%E5%88%A9%E6%B6%A6%E7%8E%87'
    print(get_html(url))