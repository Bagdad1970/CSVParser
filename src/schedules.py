import csv
from datetime import datetime, timedelta
import src.datetime_utils as dt_utils


def get_doctor_appointment_cells(*, shiftdate: datetime, begin_time: datetime.time, end_time: datetime.time, timescale: int):
    workday_time = end_time - begin_time

    appointments = workday_time.minutes() / timescale  # округлить нужно
    
    cells = []
    for i in range(0, appointments):
        cells.append( { 'dt': shiftdate, 'begin_time': begin_time + timedelta(minutes = i * timescale), 'end_time': begin_time + timedelta(minutes = (i+1) * timescale), 'free': True } )

    return cells


def get_date(shiftdate: str) -> datetime:
    base_date = datetime(1899, 12, 30)
    return dt_utils.round_time_to_nearest_hour(base_date + timedelta(days=float(shiftdate)))


def get_begin_time(*, begin_time: str, shiftdate: str) -> datetime.time:
    base_date = datetime(1899, 12, 30)
    days = float(shiftdate) + float(begin_time)
    return (base_date + timedelta(days = days)).time()


def get_end_time(*, end_time: str, shiftdate: str) -> datetime.time:
    base_date = datetime(1899, 12, 30)
    days = float(shiftdate) + float(end_time)
    return (base_date + timedelta(days = days)).time()


def get_day_schedule(row: list[str], timescale: int) -> dict:
    doctor_id = row[2]

    cells = get_doctor_appointment_cells(shiftdate=get_date(row[8]),
                                         begin_time=get_begin_time(begin_time=row[3], shiftdate=row[8]),
                                         end_time=get_end_time(end_time=row[4], shiftdate=row[8]),
                                         timescale=timescale)
    return cells


def parse_schedules(csv_file: str, doctor_timescales: dict[str, int]) -> dict:
    schedules = {}

    with open(csv_file, 'r', newline='') as csv_file:
        reader = list(csv.reader(csv_file))[2 : ]
        for row in reader:
            
            if row[2] not in schedules:
                schedules[row[2]] = []

            doctor_id = row[2]
            doctor_timescale = doctor_timescales.get(doctor_id)
            schedules[ row[2] ].append( get_day_schedule(row, doctor_timescale) )

    return schedules

