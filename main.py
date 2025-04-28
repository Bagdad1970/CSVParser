import src.doctors as doctors
import src.schedules as schedules


def main():
    _doctors = doctors.parse_doctors('archimed_doctors.sql.csv')

    doctor_timescales = doctors.match_doctors_and_timescales(_doctors)

    _schedules = schedules.parse_schedules('archimed_doctorsshedule.sql.csv', doctor_timescales)
    print(_schedules)


if __name__ == '__main__':
    main()
