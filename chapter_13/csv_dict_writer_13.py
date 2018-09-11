import csv

def csv_dict_writer(path, fieldname, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, mode='w', newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldname)
        writer.writeheader()
        writer.writerows(data)
        #for row in data:
        #    writer.writerow(row)

if __name__ == '__main__':
    data = [ "first_name,last_name,city" . split ( "," ), 
            "Tyrese,Hirthe,Strackeport" . split ( "," ), 
            "Jules,Dicki,Lake Nickolasville" . split ( "," ), 
            "Dedric,Medhurst,Stiedemannberg" . split ( "," )]
    
    my_list = []
    fieldnames1 = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames1,values))
        my_list.append(inner_dict)

    path = 'dict_output.csv'
    csv_dict_writer(path, fieldnames1, my_list)

