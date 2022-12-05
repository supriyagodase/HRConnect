from my_utils.csv_ import HandleCSV

read_csv= HandleCSV()
file_obj = read_csv.read_as_dict()
print(file_obj)
# print(read_csv.filter_data())

# for i in file_obj:
#     print(i)

# task one