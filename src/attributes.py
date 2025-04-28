from datetime import datetime


def get_talon_begin_time(row: list[str]) -> datetime.time:
    shiftdate = float(row[5])
    begin_time = float(row[3])

    return datetime.fromtimestamp(shiftdate + begin_time).time()


def get_talon_end_time(row: list[str]) -> datetime.time:
    shiftdate = float(row[5])
    end_time = float(row[4])

    return datetime.fromtimestamp(shiftdate + end_time).time()

def get_date(row: list[str]) -> datetime.date:
    shiftdate = float(row[5])
    return datetime.fromtimestamp(shiftdate).date()


def get_doctor_data(row: list[str]) -> dict:
    doctor_dict = {}

    doctor_id = row[0]

    cells = []

    name_fields = row[1:3+1]
    fullname = " ".join(map(str.strip, name_fields)).strip()


    doctor_dict[f'doctor_id_{doctor_id}'] = { 'efio': fullname, 'espec': '', 'cells': cells }

    return doctor_dict