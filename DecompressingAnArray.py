"""
Задача на разжатие массива. 
У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах. 
Для эффективности дни проката хранятся периодами дат. Например, прокат фильма проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля:
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        data_list = []
        for l_tumle in self.dates:
            t_delta = l_tumle[1]-l_tumle[0]
            data_list += [l_tumle[0] + timedelta(days=x) for x in range(t_delta.days+1)]
        return data_list


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
