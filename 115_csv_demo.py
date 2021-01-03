import csv


def read_text():
    # raw
    with open(r"C:\Users\JaiDog\Documents\GitHub\Python-Language\All_docs\rio2016.csv") as f:
        data = f.read()
        print(type(data))
        print(data)


def read_csv():
    # raw
    with open(r"C:\Users\JaiDog\Documents\GitHub\Python-Language\All_docs\rio2016.csv", newline="") as f:
        data = csv.reader(f)
        # print(type(data))
        # print(data)
        for row in data:
            # print(row)
            print("{:25}: {:2} {:2} {:2} = {:3}".format(row[0], row[1], row[2], row[3],
                                                        int(row[1]) + int(row[2]) + int(row[3])))


def read_csv2():
    # raw
    with open(r"C:\Users\JaiDog\Documents\GitHub\Python-Language\All_docs\rio2016tab.txt", newline="") as f:
        # delimiter
        data = csv.reader(f, delimiter="\t")
        # print(type(data))
        # print(data)
        for row in data:
            # print(row)
            print("{:25}: {:2} {:2} {:2} = {:3}".format(row[0], row[1], row[2], row[3],

                                                        int(row[1]) + int(row[2]) + int(row[3])))


def read_csv_header():
    # raw
    with open(r"C:\Users\JaiDog\Documents\GitHub\Python-Language\All_docs\rio2016_header_column.csv", newline="") as f:
        data = csv.DictReader(f)
        print(type(data))
        print(data)
        print(data.fieldnames)
        for row in data:
            # print(row)
            print(row["country"], row["gold"])
        # for row in data:
        #     # print(row)
        #     print("{:25}: {:2} {:2} {:2} = {:3}".format(row[0], row[1], row[2], row[3],
        #                                                 int(row[1]) + int(row[2]) + int(row[3])))


# read_text()
# read_csv()
# read_csv2()
read_csv_header()
