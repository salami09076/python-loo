import crawling as cr
import step as st
import dml as dl
import interval as iv


# INSERT INTO [T_ORIGIN && T_STEP_ORIGIN && T_INTERVAL_ORIGIN && T_STEP_INTERVAL_ORIGIN]
def put_the_current_wins_into_t_origin():
    # crawling
    drw_dict = cr.get_current_drw()

    # origin step calculation / insert preparation / insert commit
    # step_list = st.step_by_one(drw_dict['drw_numbers'])
    # for step in step_list:
    #     step.insert(0, int(drw_dict['drw_id']))
    # dl.insert_into_t_step_origin(step_list)

    # origin interval calculation / insert preparation / insert commit
    # interval_list = iv.get_interval(drw_dict['drw_numbers'])  # argument : list
    # drw = interval_list
    # drw.insert(0, int(drw_dict['drw_id']))
    # dl.insert_into_t_interval_origin(drw)

    # TODO interval step calculation


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
