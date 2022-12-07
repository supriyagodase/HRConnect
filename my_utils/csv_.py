import csv
from csv import reader

class HandleCSV():
    filename = (r"D:\Python Lecture\CSV\employees.csv")

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename,"r")as foo:
            # print(dir(foo))# readmode
            return foo.readline()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename,"r")as bar:
            yield bar.readline()

    @classmethod
    # new_dict = {}
    def read_as_dict(cls):
        with open(cls.filename) as csvfile:
            data=csv.DictReader(csvfile)
            emp_list=[]
            for i in data:
                new_dict = {}
                for key,val in i.items():
                    if key in ['FIRST_NAME', 'LAST_NAME', 'PHONE_NUMBER', 'SALARY']:
                        # print(key, val)
                        if key == 'PHONE_NUMBER':
                            new_dict[key] =val.replace('.', '')
                        else:
                            new_dict[key]= val
                    # if 'SALARY' >int(9000):
                    # new_dict[key]=val
                    # list.append(new_dict)
                # print(new_dict)
                if int(new_dict['SALARY']) > 9000:
                    emp_list.append(new_dict)
            # print(len(emp_list))
            return emp_list

    def filter_data(list,):
        for i in list:
            print(i[7])


                # if i.get('SALARY') > int(9000):
                #     return i



if __name__ == "__main__" :
    obj = HandleCSV()
    # obj1= obj.read_entire_csv()
    # print(obj1)
    # print(type(obj1))
    # obj2 = obj.read_csv_line_by_line()
    print(obj.read_as_dict())
    # print(next(obj2))
    # for i in obj2:
    #     print(next(obj2))




