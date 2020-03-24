import sqlite3


def insert_into_t_origin(drw):
    try:
        sql = 'INSERT INTO T_ORIGIN VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        conn = sqlite3.connect('loo.db')
        cur = conn.cursor()
        cur.execute(sql, drw)
        conn.commit()
        print('INSERT COMMITTED')

    except Exception as e:
        print('INSERT FAILED')
        print(e)

    finally:
        conn.close()


def insert_into_t_interval_origin(drw):
    try:
        sql = 'INSERT INTO T_INTERVAL_ORIGIN (iid, i1, i2, i3, i4, i5, i6, ib) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        conn = sqlite3.connect('loo.db')
        cur = conn.cursor()
        cur.execute(sql, drw)
        conn.commit()
        print('INSERT ALL COMMITTED')

    except Exception as e:
        print('INSERT ALL FAILED')
        print(e)

    finally:
        conn.close()


def insert_into_t_step_interval_origin(interval_step_list):
    try:
        sql = 'INSERT INTO T_STEP_INTERVAL_ORIGIN (iid, is1, is2, is3, is4, is5, is6) VALUES(?, ?, ?, ?, ?, ?, ?)'
        conn = sqlite3.connect('loo.db')
        cur = conn.cursor()
        cur.executemany(sql, interval_step_list)
        conn.commit()
        print('INSERT ALL COMMITTED')

    except Exception as e:
        print('INSERT ALL FAILED')
        print(e)

    finally:
        conn.close()


def insert_into_t_step_origin(step_list):
    try:
        sql = 'INSERT INTO T_STEP_ORIGIN (did, b1, b2, b3, b4, b5, b6, bb) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        conn = sqlite3.connect('loo.db')
        cur = conn.cursor()
        cur.executemany(sql, step_list)
        conn.commit()
        print('INSERT ALL COMMITTED')

    except Exception as e:
        print('INSERT ALL FAILED')
        print(e)

    finally:
        conn.close()


def insert_all_into_t_origin(drw):
    try:
        sql = 'INSERT INTO T_ORIGIN VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        conn = sqlite3.connect('loo.db')
        cur = conn.cursor()
        cur.executemany(sql, drw)
        conn.commit()
        print('INSERT ALL COMMITTED')

    except Exception as e:
        print('INSERT ALL FAILED')
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    drw = ((12, 2, 3, 5, 6, 7, 8, 8), (13, 2, 3, 5, 6, 7, 8, 8), (14, 2, 3, 5, 6, 7, 8, 8), (15, 2, 3, 5, 6, 7, 8, 8))
    #insert_into_t_origin(drw)
    insert_all_into_t_origin(drw)