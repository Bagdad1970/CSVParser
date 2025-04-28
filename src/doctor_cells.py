from datetime import datetime, timdelta


def create_doctor_appointment_cells(begin_time: datetime.time, end_time: datetime.time, timescale: int):
    workday_time = end_time - begin_time

    appointments = workday_time.minutes() / timescale  # округлить нужно
    
    cells = []
    for i in range(0, appointments):
        cells.append( { 'dt': , 'begin_time': begin_time + timedelta(minutes = i * timescale), 'end_time': begin_time + timedelta(minutes = (i+1) * timescale), 'free': True } )

    return cells
