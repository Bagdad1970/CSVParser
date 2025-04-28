import csv


def calculate_timescale(*, timescale: str, max_time: str, default: int=30) -> int:
    timescale = int(timescale) if timescale != '' else 0
    if timescale > 0:
        return timescale

    max_time = int(max_time) if max_time != '' else 0
    if max_time > 0:
        return max_time

    return default


def get_doctor(row: list[str]) -> dict:
    return { "fullname": row[5], "espec": '', 'timescale': calculate_timescale(timescale=row[7], max_time=row[8]) }

def match_doctors_and_timescales(doctors: dict) -> dict:
    return { doctor_id : info.get('timescale') for doctor_id, info in doctors.items() }


def parse_doctors(csv_file: str) -> dict:
    doctors = {}

    with open(csv_file, 'r', newline='') as csv_file:
        reader = list(csv.reader(csv_file))[2 : ]
        for row in reader:
            doctors[ row[0] ] = get_doctor(row)

    return doctors
