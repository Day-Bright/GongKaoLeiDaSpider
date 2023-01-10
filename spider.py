import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.utils import formataddr

import requests
from bs4 import BeautifulSoup

import config as config


def spider(url, page_num):
    response = requests.get(url=url+str(page_num), headers=config.headers)
    soup = BeautifulSoup(response.content, 'lxml', from_encoding='utf-8')
    link_list = soup.select('.notice-list li')
    result = ""
    for i in link_list:
        href = i.find('a')['href']
        title = i.find('a').text
        time = i.find("time").text
        if ("-" in time) and ((datetime.now().date()-datetime.strptime(time, "%Y-%m-%d").date()).days > config.time_span):
            page_num = 0
            break
        k = 1
        for j in config.filter_words:
            if j in title:
                k = 0
        if k:
            result = result+href+"   "+title+"   "+time+"\n"
    return result, page_num


def mail(inf):
    msg = MIMEText(inf, 'plain', 'utf-8')
    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['From'] = formataddr([config.my_sender, config.my_sender])
    # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['To'] = formataddr([config.my_user, config.my_user])
    msg['Subject'] = "考试信息"  # 邮件的主题，也可以说是标题
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
    server.login(config.my_sender, config.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
    server.sendmail(config.my_sender, [config.my_user, ], msg.as_string())
    # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接


def run():
    page_num = 1
    inf = ""
    while True:
        url = ""
        if len(config.my_category) == 0:
            url = "https://www.gongkaoleida.com/area/{my_province}?page=".format(
                my_province=config.province_num[config.my_province])
        else:
            category_str = ""
            for j in config.my_category:
                category_str = str(config.category[j])+","+category_str
            url = "https://www.gongkaoleida.com/area/{my_province}-0-0-{my_category}-0?page=".format(
                my_province=config.province_num[config.my_province], my_category=category_str[:-1])
        result = spider(url, page_num)
        if result[1] == 0:
            inf += result[0]
            break
        else:
            page_num += 1
            inf += result[0]
    print(inf)
    mail(inf)


run()
