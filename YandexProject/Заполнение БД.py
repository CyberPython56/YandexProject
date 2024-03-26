import sqlite3
from datetime import *
from random import *
import names


def can_booking(time_start, time_finish, computer):
    with sqlite3.connect('YandexProject.sqlite') as con:
        cur = con.cursor()
        bookings = cur.execute(f"""SELECT * FROM booking WHERE computerid = {computer}
            AND date = '{0}'""").fetchall()
        for i in bookings:
            flag_time = False
            check_time(time_start, time_finish, i[4], i[5])
            if flag_time:
                global flag_can_book
                flag_can_book = False


def check_time(t0_self, t1_self, t0_other, t1_other):
    time_start = tuple([int(t0_self.split(':')[0]), int(t0_self.split(':')[1])])
    time_finish = tuple([int(t1_self.split(':')[0]), int(t1_self.split(':')[1])])
    time_start_other = tuple([int(t0_other.split(':')[0]), int(t0_other.split(':')[1])])
    time_finish_other = tuple([int(t1_other.split(':')[0]), int(t1_other.split(':')[1])])
    time_start = time(time_start[0], time_start[1])
    time_finish = time(time_finish[0], time_finish[1])
    time_start_other = time(time_start_other[0], time_start_other[1])
    time_finish_other = time(time_finish_other[0], time_finish_other[1])
    if (time_start_other < time_start < time_finish_other \
        or time_start_other < time_finish < time_finish_other) \
            or (time_start <= time_start_other and time_finish >= time_finish_other) \
            or (time_start >= time_start_other and time_finish <= time_finish_other):
        global flag_time
        flag_time = True

for i in range(50):
    with sqlite3.connect('YandexProject.sqlite') as con:
        cur = con.cursor()
        id = randint(0, 242)
        name = names.get_full_name()
        date = randint(12, 30)
        if date >= 10:
            date = str(date) + '.11.2021'
        else:
            date = '0' + str(date) + '.11.2021'
        start_time0 = randint(10, 18)
        start_time1 = choice(['00', '15', '30', '45'])
        duration = randint(2, 5)
        flag_can_book = True
        start_time = str(start_time0) + ':' + start_time1
        finish_time = str(int(start_time.split(':')[0]) + duration) + ':' + start_time.split(':')[1]
        delta = int(finish_time.split(':')[0]) - int(start_time.split(':')[0])
        can_booking(start_time, finish_time, id)
        if flag_can_book:
            price = cur.execute(f"""SELECT price FROM halls WHERE hallid = (SELECT hallid FROM computers WHERE computerid = {id})""").fetchone()[0]
            cur.execute(f"""INSERT INTO booking(computerid, name, date, time_start, time_finish, full_price) 
                    VALUES({id}, '{name}', '{date}', '{start_time}', '{finish_time}', {int(price) * delta})""")








