import csv

def csv_reader(file_obj):
    """
    Read a CSV file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))
        #print(row)

if __name__ == '__main__':
    csv_path = r'C:\Rafi\py_tut\mousevspython\TB_data_dictionary_2018-08-28.csv'
    with open(csv_path, 'r') as f_obj:
        csv_reader(f_obj)
