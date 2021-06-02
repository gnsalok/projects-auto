import csv


with open('tap_test_copy.csv') as in_file:
    with open('out.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(row):
                writer.writerow(row)