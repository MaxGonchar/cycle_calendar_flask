from datetime import date

from server.models import Date, CycleEvent

MOCK_DATES = [
    Date(date_=date(2021, 1, 1),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 2, 2),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 3, 3),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 4, 4),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 5, 5),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 6, 6),
         cycle_event=[CycleEvent(type_='cycle_start')]),
]
MOCK_PREDICTED_CYCLE_EVENTS = {
    date(2021, 7, 7): ['predicted_start0'],
    date(2021, 7, 8): ['predicted_start1'],
    date(2021, 7, 6): ['predicted_start1'],
    date(2021, 7, 5): ['predicted_start2'],
    date(2021, 7, 9): ['predicted_start2'],
    date(2021, 7, 10): ['predicted_start3'],
    date(2021, 7, 4): ['predicted_start3'],
    date(2021, 7, 3): ['predicted_start4'],
    date(2021, 7, 11): ['predicted_start4'],
    date(2021, 6, 16): ['cycle_middle'],
    date(2021, 6, 17): ['cycle_middle'],
    date(2021, 6, 18): ['cycle_middle'],
    date(2021, 6, 19): ['cycle_middle'],
    date(2021, 6, 20): ['cycle_middle']
}
MOCK_PREDICTED_CYCLE_EVENTS_PLUS_DATE = {
    date(2021, 8, 7): ['predicted_start0'],
    date(2021, 8, 8): ['predicted_start1'],
    date(2021, 8, 6): ['predicted_start1'],
    date(2021, 8, 5): ['predicted_start2'],
    date(2021, 8, 9): ['predicted_start2'],
    date(2021, 8, 10): ['predicted_start3'],
    date(2021, 8, 4): ['predicted_start3'],
    date(2021, 8, 11): ['predicted_start4'],
    date(2021, 8, 3): ['predicted_start4'],
    date(2021, 7, 17): ['cycle_middle'],
    date(2021, 7, 18): ['cycle_middle'],
    date(2021, 7, 19): ['cycle_middle'],
    date(2021, 7, 20): ['cycle_middle'],
    date(2021, 7, 21): ['cycle_middle']
}
MOCK_DATE_NOW = date(2021, 7, 1)

MOCK_MONTH_DATA = {
    'days': [{'date': '2021-06-28', 'events': []},
             {'date': '2021-06-29', 'events': []},
             {'date': '2021-06-30', 'events': []},
             {'date': '2021-07-01', 'events': []},
             {'date': '2021-07-02', 'events': []},
             {'date': '2021-07-03', 'events': ['predicted_start4']},
             {'date': '2021-07-04', 'events': ['predicted_start3']},
             {'date': '2021-07-05', 'events': ['predicted_start2']},
             {'date': '2021-07-06', 'events': ['predicted_start1']},
             {'date': '2021-07-07', 'events': ['predicted_start0']},
             {'date': '2021-07-08', 'events': ['predicted_start1']},
             {'date': '2021-07-09', 'events': ['predicted_start2']},
             {'date': '2021-07-10', 'events': ['predicted_start3']},
             {'date': '2021-07-11', 'events': ['predicted_start4']},
             {'date': '2021-07-12', 'events': []},
             {'date': '2021-07-13', 'events': []},
             {'date': '2021-07-14', 'events': []},
             {'date': '2021-07-15', 'events': []},
             {'date': '2021-07-16', 'events': []},
             {'date': '2021-07-17', 'events': []},
             {'date': '2021-07-18', 'events': []},
             {'date': '2021-07-19', 'events': []},
             {'date': '2021-07-20', 'events': []},
             {'date': '2021-07-21', 'events': []},
             {'date': '2021-07-22', 'events': []},
             {'date': '2021-07-23', 'events': []},
             {'date': '2021-07-24', 'events': []},
             {'date': '2021-07-25', 'events': []},
             {'date': '2021-07-26', 'events': []},
             {'date': '2021-07-27', 'events': []},
             {'date': '2021-07-28', 'events': []},
             {'date': '2021-07-29', 'events': []},
             {'date': '2021-07-30', 'events': []},
             {'date': '2021-07-31', 'events': []},
             {'date': '2021-08-01', 'events': []}],
    'month': 'July',
    'year': 2021
}
MOCK_DATES_EVENTS = {
    date(2021, 1, 1): ['cycle_start'],
    date(2021, 2, 2): ['cycle_start'],
    date(2021, 3, 3): ['cycle_start'],
    date(2021, 4, 4): ['cycle_start'],
    date(2021, 5, 5): ['cycle_start'],
    date(2021, 6, 6): ['cycle_start'],
    date(2021, 6, 16): ['cycle_middle'],
    date(2021, 6, 17): ['cycle_middle'],
    date(2021, 6, 18): ['cycle_middle'],
    date(2021, 6, 19): ['cycle_middle'],
    date(2021, 6, 20): ['cycle_middle'],
    date(2021, 7, 3): ['predicted_start4'],
    date(2021, 7, 4): ['predicted_start3'],
    date(2021, 7, 5): ['predicted_start2'],
    date(2021, 7, 6): ['predicted_start1'],
    date(2021, 7, 7): ['predicted_start0'],
    date(2021, 7, 8): ['predicted_start1'],
    date(2021, 7, 9): ['predicted_start2'],
    date(2021, 7, 10): ['predicted_start3'],
    date(2021, 7, 11): ['predicted_start4']
}
MOCK_DATES_EVENTS_PLUS_DAY = {
    date(2021, 1, 1): ['cycle_start'],
    date(2021, 2, 2): ['cycle_start'],
    date(2021, 3, 3): ['cycle_start'],
    date(2021, 4, 4): ['cycle_start'],
    date(2021, 5, 5): ['cycle_start'],
    date(2021, 6, 6): ['cycle_start'],
    date(2021, 7, 7): ['cycle_start'],
    date(2021, 7, 17): ['cycle_middle'],
    date(2021, 7, 18): ['cycle_middle'],
    date(2021, 7, 19): ['cycle_middle'],
    date(2021, 7, 20): ['cycle_middle'],
    date(2021, 7, 21): ['cycle_middle'],
    date(2021, 8, 3): ['predicted_start4'],
    date(2021, 8, 4): ['predicted_start3'],
    date(2021, 8, 5): ['predicted_start2'],
    date(2021, 8, 6): ['predicted_start1'],
    date(2021, 8, 7): ['predicted_start0'],
    date(2021, 8, 8): ['predicted_start1'],
    date(2021, 8, 9): ['predicted_start2'],
    date(2021, 8, 10): ['predicted_start3'],
    date(2021, 8, 11): ['predicted_start4']
}
