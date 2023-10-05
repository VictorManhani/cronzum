import typing
import datetime
from cronzun import Cronzun

def test1():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 23, 31, 47)

def test2():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('0 * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 23, 32, 0)

def test3():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('1 * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 23, 32, 1)

def test4():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('30 * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 23, 32, 30)

def test5():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('59 * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 23, 32, 59)

def test5():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* 0 * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 0, 0, 47)

def test6():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* 1 * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 0, 1, 47)

def test7():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* 30 * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 0, 30, 47)

def test8():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* 59 * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 28, 0, 59, 47)

def test9():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * 0 * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 29, 0, 31, 47)

def test10():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * 1 * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 29, 1, 31, 47)

def test11():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * 12 * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 29, 12, 31, 47)

def test12():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * 23 * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 9, 29, 23, 31, 47)

def test13():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * 1 * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 1, 0, 0, 0)

def test14():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * 15 * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 15, 0, 0, 0)

def test15():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * 30 * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 30, 0, 0, 0)

def test16():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * 1 ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2024, 1, 1, 0, 0, 0)

def test17():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * 6 ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2024, 6, 1, 0, 0, 0)

def test18():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * 12 ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2024, 12, 1, 0, 0, 0)

def test19():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * * ? 2024', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2024, 1, 1, 0, 0, 0)

def test20():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * * ? 5000', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(5000, 1, 1, 0, 0, 0)

def test21():
    dt = datetime.datetime(2023, 9, 28, 23, 31, 46)
    cron = Cronzun('* * * * * ? 9999', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(9999, 1, 1, 0, 0, 0)

def test22():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 0 * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 2, 10, 0, 0)

def test23():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 0 0 * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 3, 0, 0, 0)

def test24():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 0 0 1 * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 11, 1, 0, 0, 0)

def test25():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 0 0 1 1 ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2024, 1, 1, 0, 0, 0)

def test26():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 0 0 1 1 ? 2025', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2025, 1, 1, 0, 0, 0)

def test27():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 5 0 * 8 ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2024, 8, 1, 0, 5, 0)

def test28():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 15 14 1 * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 11, 1, 14, 15, 0)

def test29():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 0 22 ? * 1-5 *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 2, 22, 0, 0)

def test30():
    dt = datetime.datetime(2023, 10, 2, 9, 30, 30)
    cron = Cronzun('0 5 4 ? * sun *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 8, 4, 5, 0)

def test30():
    dt = datetime.datetime(2023, 10, 2, 12, 2, 20)
    cron = Cronzun('5 * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 2, 12, 3, 5)

def test31():
    dt = datetime.datetime(2023, 10, 2, 12, 2, 0)
    cron = Cronzun('10 * * * * ? *', dt)
    cnd = cron.get_next_date()
    print(cnd)
    assert cnd == datetime.datetime(2023, 10, 2, 12, 2, 10)