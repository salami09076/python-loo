import sqlite3


def create_t_origin_table():
    conn = sqlite3.connect('loo.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE T_ORIGIN (
                    did INTEGER,
                    b1 INTEGER,
                    b2 INTEGER,
                    b3 INTEGER,
                    b4 INTEGER,
                    b5 INTEGER,
                    b6 INTEGER,
                    bb INTEGER,
                    PRIMARY KEY (did),
                    CHECK(b1 > 0 AND b1 < 46
                      AND b2 > 0 AND b2 < 46
                      AND b3 > 0 AND b3 < 46
                      AND b4 > 0 AND b4 < 46
                      AND b5 > 0 AND b5 < 46
                      AND b6 > 0 AND b6 < 46
                      AND bb > 0 AND bb < 46)
                    )''')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_t_origin_table()
