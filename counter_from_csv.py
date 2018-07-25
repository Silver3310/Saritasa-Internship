import csv, argparse


def name_via_parsing():
    # creating a parser
    parser = argparse.ArgumentParser(description='Process CSV file')
    # adding arguments
    parser.add_argument('input_file', metavar='csv file', type=str,
                        help='an input csv file to read the dictionary')

    args = parser.parse_args()

    return args.input_file


def dict_to_count(file_name):
    records = list()
    with open('input.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)
    return records


def counter(records_list, key, value):
    count = 0
    for each in records_list:
        if each[key] == value:
            count += 1
    return dict(key=key, value=value, count=count)


def list_counter(records):
    c_list = list()
    result = dict()
    keys = records[0].keys()
    for each in records:
        for k in keys:
            if k not in result.keys():
                result[k] = list()
            result[k].append(each[k])
            

def main():
    # get the name of the input file
    file_name = name_via_parsing()
    records = dict_to_count(file_name)
    list_counter(records)


if __name__ == '__main__':
    main()
