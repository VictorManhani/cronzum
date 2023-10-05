# cronzun

This cron module was created with the goal of providing a simple cron API, all in one file. 

It was created from the concept of TDD, i.e. first create a test, run it with pytest, it will fail. Then, create or refactor the implementation to make the test pass, without breaking the other tests. 

This project was created without ChatGPT and without the use of any framework. 

Give me your tips and tricks on how this module could improve.

# How to use
```py
from cronzun import Cronzun

from_date = datetime.datetime(2023, 5, 10, 2, 0, 0)

cron = Cronzun('20 * * * * ? *', from_date)

next_date = cron.get_next_date()
print('from date:', from_date)
print('next date:', next_date)
```

# How to test
`pytest .\test_cronzun.py`