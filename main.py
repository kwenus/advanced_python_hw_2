import csv
from pprint import pprint
import re
from patterns import *


if __name__ == '__main__':

    with open('phonebook_raw.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        contact_list = list(data)

        new_list = []
        duplicate_list = []
        for row in contact_list:
            new_row = ",".join(" ".join(row[:3]).split(" ")[:3] + row[3:])
            new_list.append(re.sub(pattern_adv, subs_adv, (re.sub(pattern_phone, subs_phone, new_row))).split(","))
            for row_1 in new_list:
                for row_2 in new_list:
                    if row_1 != row_2 and row_1[:2] == row_2[:2]:
                        for ind in range(len(row_1)):
                            if row_1[ind] == '':
                                row_1[ind] = row_2[ind]
                        if row_1 not in duplicate_list:
                            duplicate_list.append(row_1)
        for elem in duplicate_list:
            new_list.remove(elem)

        with open("phonebook.csv", "w", encoding="utf-8") as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(new_list)
