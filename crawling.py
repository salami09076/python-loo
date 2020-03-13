from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import re


def get_current_drw():
    try:
        result_dict = dict()
        main_url = 'https://dhlottery.co.kr/common.do?method=main'
        html = urlopen(main_url).read()
        soup = BeautifulSoup(html, 'html.parser')

        info = soup.find('div', class_='content')
        drw_id = info.h3.a.strong.text
        drw_date = str(info.h3.a.span.next_sibling.next_sibling.text).replace('-', '')
        drw_numbers = re.findall('\d+', info.p.a.text)

        result_dict['drw_id'] = drw_id
        result_dict['drw_date'] = drw_date
        result_dict['drw_numbers'] = drw_numbers

    except Exception as e:
        print('동행복권 에러')
        print(e)
        result_dict = None

    return result_dict


def get_single_drw(drw_id):
    try:
        result_dict = dict()
        url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=' + str(drw_id)
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        div = soup.find('div', class_='win_result')
        drw_id = ''.join(filter(str.isdigit, div.h4.strong.text))
        drw_date = re.findall('\d+', div.p.text)
        drw_date = ''.join(drw_date)
        drw_numbers = soup.select('div.nums span')
        drw_numbers = list(map(lambda x: x.text, drw_numbers))

        result_dict['drw_id'] = drw_id
        result_dict['drw_date'] = drw_date
        result_dict['drw_numbers'] = drw_numbers

    except Exception as e:
        print('동행복권 에러')
        print(e)
        result_dict = None

    return result_dict


def get_total_drw():
    try:
        result_list = list()
        main_url = 'https://dhlottery.co.kr/common.do?method=main'
        html = urlopen(main_url).read()
        soup = BeautifulSoup(html, 'html.parser')

        info = soup.find('div', class_='content')
        drw_id = int(info.h3.a.strong.text)             # 최근 추첨회차

        for i in range(1, drw_id + 1):
            result_list.append(get_single_drw(i))

    except Exception as e:
        print('동행복권 에러')
        print(e)
        result_list = None

    return result_list


def get_some_drw(st_drw_id, ed_drw_id):
    result_list = list(get_single_drw(i) for i in range(st_drw_id, ed_drw_id+1))
    return result_list
