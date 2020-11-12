import csv

def readCSV():
    with open('MyFriends.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} birthday in {row["birth day"]} , and like {row["color"]} color.')
            line_count += 1
        print(f'Processed {line_count} lines.')

def writeCSV():
    with open('MyFriends.txt', mode='a') as Like_file:
        Like_writer = csv.writer(Like_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        Like_writer.writerow(['firn', 'monday', 'pink'])
        Like_writer.writerow(['fah', 'friday', 'green'])

readCSV()
#writeCSV()