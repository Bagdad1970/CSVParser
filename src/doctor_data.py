import src.attributes as attrs


doctor_cells = { **attrs.parse_talons('/home/user/Downloads/archimed_talons.sql.csv'),
                 **attrs.parse_doctor_schedules('/home/user/Downloads/archimed_doctorsshedule.sql.csv')
                }

def get_doctor_data(row: list[str]) -> dict:
    doctor_dict = {}

    doctor_id = row[0]
    fullname = row[5].strip()

    timescale = attrs.get_doctor_timescale(row)

    cells = doctor_cells.get(doctor_id)



    doctor_dict[f'doctor_id_{doctor_id}'] = { 'efio': fullname, 'espec': '', 'cells': cells }

    return doctor_dict