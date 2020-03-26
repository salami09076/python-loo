import crawling as cr
import step as st
import dml as dl
import interval as iv
import multiprocessing as mp


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
    interval_list = iv.get_interval(drw_dict['drw_numbers'])  # argument : list
    interval_step_list = interval_list
    # interval_list.insert(0, int(drw_dict['drw_id']))
    # dl.insert_into_t_interval_origin(interval_list)

    # interval step calculation / insert preparation / insert commit
    interval_step_list = st.step_by_one(interval_step_list)
    for step in interval_step_list:
        step.insert(0, int(drw_dict['drw_id']))
    dl.insert_into_t_step_interval_origin(interval_step_list)


def put_the_bulk_wins_into_t_origin(st_drw_id, ed_drw_id):

    # crawling
    drw_dict_list = cr.get_some_drw(st_drw_id, ed_drw_id)

    # origin / insert preparation / insert commit
    drw = list()
    for drw_dict in drw_dict_list:
        temp = drw_dict['drw_numbers']
        temp.insert(0, int(drw_dict['drw_id']))
        drw.append(temp)
    dl.insert_all_into_t_origin(drw)

    # origin step calculation / insert preparation / insert commit
    for drw_dict in drw_dict_list:
        step_list = st.step_by_one(drw_dict['drw_numbers'])
        for step in step_list:
            step.insert(0, int(drw_dict['drw_id']))
        dl.insert_into_t_step_origin(step_list)

    # origin interval calculation / insert preparation / insert commit
    for drw_dict in drw_dict_list:
        interval_list = iv.get_interval(drw_dict['drw_numbers'])  # argument : list
        interval_step_list = interval_list
        interval_list.insert(0, int(drw_dict['drw_id']))
        dl.insert_into_t_interval_origin(interval_list)

    # interval step calculation / insert preparation / insert commit
        interval_step_list = st.step_by_one(interval_step_list)
        for step in interval_step_list:
            step.insert(0, int(drw_dict['drw_id']))
        dl.insert_into_t_step_interval_origin(interval_step_list)


def put_the_all_wins_into_t_origin():
    drw_dict = cr.get_current_drw()
    drw_id = int(drw_dict['drw_id'])
    cpu = mp.cpu_count()

    div, mod = divmod(drw_id, cpu)
    print(mod)
    num_arr = list()

    for i in range(cpu):
        num_arr.append(div * i)
    num_arr.append(drw_id)

    procs = []

    for i, num in enumerate(num_arr, 1):
        if i < len(num_arr):
            proc = mp.Process(target=put_the_bulk_wins_into_t_origin, args=(num+1, num_arr[i]))
            procs.append(proc)
            proc.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    # put_the_all_wins_into_t_origin()
    put_the_bulk_wins_into_t_origin(299, 300)
    # print(put_the_current_wins_into_t_origin())
