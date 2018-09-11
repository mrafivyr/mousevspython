import csv

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')

    for line in reader:
        print(line['first_name'])
        print(line['last_name'])


if __name__ == '__main__':
    with open(r'C:\Rafi\py_tut\mousevspython\data.csv', mode='r') as f_obj:
        csv_dict_reader(f_obj)
