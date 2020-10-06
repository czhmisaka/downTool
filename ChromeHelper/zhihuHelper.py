import re
import os
import requests
import json
import time

def saveHistory(data):
    with open('History.txt','w',encoding='utf-8') as f:
        for x in data:
            f.write(x+'\n')

def getDesktopPath():
    '''
    获取桌面路径
    '''
    return os.path.join(os.path.expanduser('~'),"Desktop")+'/'

def zhihuMain():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}

    # 知乎问题id
    question_id = input('问题 id >')
    interval = 20
    offset = 0
    rank = 100
    novels_count = dict()


    p = re.compile(r'<p>.+?</p>')git
    data = []
    while True:
        print(f'答案数 {offset} 到 {offset + interval}')
        # 知乎获取回答分页API
        url = f'https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=content&limit={interval}&offset={offset}&sort_by=default'
        html = requests.get(url, headers=headers)
        answers = html.json()['data']
        if len(answers) == 0:
            break
        for answer in answers:
            results = set(re.findall(p, answer['content']))
            for x in results:
                if len(x.split('<p>'))>=1:
                    word = x.split('<p>')[1].split('</p>')[0]
                    data.append(word)
                else:
                    data.append(x)
        offset += interval
    saveHistory(data)

zhihuMain()