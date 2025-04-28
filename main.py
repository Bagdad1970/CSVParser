import csv
import src.doctor_data as doctor_data


def parse_schedule_csv_file(csv_file: str):
    parsed_csv = {}

    with open(csv_file, 'r', newline='') as csv_file:
        reader = list(csv.reader(csv_file))[2:]
        for row in reader:
            print(doctor_data.get_doctor_data(row))


def main():
    filename = '/home/user/Downloads/archimed_doctors.sql.csv'
    parse_schedule_csv_file(filename)


if __name__ == '__main__':
    main()