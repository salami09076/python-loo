import crawling as cr
import step as st
import dml as dl
import interval as iv


# 최근 추첨정보 db에 넣기
def put_the_current_wins_into_t_origin():
    # crawling
    drw_dict = cr.get_current_drw()

    # step calculation / insert preparation / insert commit
    step_list = st.step_by_one(drw_dict['drw_numbers'])
    dl.insert_into_t_step_origin(drw_dict['drw_id'], step_list)

    # interval 계산
    # interval_list = iv.get_interval(drw_dict['drw_numbers'])

    # print(step_list)
    # print(interval_list)

    # insert 준비 (회차와 당첨번호 dict를 list로 만듦)
    drw = list()
    drw = drw_dict['drw_numbers']
    drw.insert(0, int(drw_dict['drw_id']))

    # insert (db에 넣음)
    #dl.insert_into_t_origin(drw)


def put_the_bulk_wins_into_t_origin(st_drw_id, ed_drw_id):

    drw_dict_list = cr.get_some_drw(st_drw_id, ed_drw_id)

    # prepare insert (회차와 당첨번호 dict를 list로 만듦)
    drw = list()
    for drw_dict in drw_dict_list:
        temp = list()
        temp = drw_dict['drw_numbers']
        temp.insert(0, int(drw_dict['drw_id']))
        drw.append(temp)

    dl.insert_all_into_t_origin(drw)


if __name__ == '__main__':
    # print(put_the_bulk_wins_into_t_origin(800, 898))
    print(put_the_current_wins_into_t_origin())
