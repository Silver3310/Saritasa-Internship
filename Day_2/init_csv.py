from faker import Faker
import csv


def init_csv_file(source):
    with open('input.csv', 'w') as csv_file:
        # here we specify the field names of our records
        field_names = ['name', 'success', 'email']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        # the first row will be the names of the fields
        #  in order to make it clear
        # what the following rows mean
        writer.writerow({'name': 'name', 'success': 'success',
                         'email': 'email'})
        # the following rows
        for _ in range(10000):
            writer.writerow({'name': source.name(),
                             'success': source.boolean(),
                             'email': source.email()})


def main():
    fake = Faker()
    init_csv_file(fake)


if __name__ == '__main__':
    main()
