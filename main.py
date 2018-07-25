from faker import Faker
import csv


def init_csv_file(source):
    with open('input.csv', 'w') as csv_file:
        field_names = ['name', 'success']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writerow({'name': 'name', 'success': 'success'})
        for i in range(10000):
            writer.writerow({'name': source.name(), 'success': source.boolean()})


def main():
    fake = Faker()
    init_csv_file(fake)


if __name__ == '__main__':
    main()



