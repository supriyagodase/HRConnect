import csv
from csv import reader
from datetime import datetime

class HandleCSV():
    filename = (r"D:\Python Lecture\CSV\employees.csv")
    @classmethod
    def read_as_dict(cls):
        with open(cls.filename) as csvfile:
            data = csv.reader(csvfile)
            # for i in data:
            #     print(i)
            headers = next(data)
            # print(headers)
            return [dict(zip(headers, i)) for i in data]

    @classmethod
    def task_one(cls):
        list_ = cls.read_as_dict()
        list2 = []
        for i in list_: # dictionary
            if int(i.get('SALARY')) > 9000:
                list2.append({'name': i.get('FIRST_NAME')+''+i.get('LAST_NAME'), 'email': i.get('EMAIL'),
                              'phone_number': i.get('PHONE_NUMBER').replace('.', '')})
        return list2

    @classmethod
    def date_convert(cls, date) -> str:
        """
        convert received date in date format
        :param date: date in format '21-Jun-07'
        :return:date in format yyyy-mm-dd
        """
        date_format = "%d-%b-%y"   # date format for '21-Jun-07'
        hire_date = datetime.strptime(date, date_format)  # return 2018-12-31 00:00:00
        hire_date = hire_date.date()  # convert into 2018-12-31

        return str(hire_date)

    @classmethod
    def task_two(cls):
        emp_details = {} #dep id bet 30 and 110 salary gret than 4200
        for i in cls.read_as_dict():
            if 30 <= int(i.get('DEPARTMENT_ID')) <= 110 and int(i.get('SALARY')) > 4200:
                hire_date = cls.date_convert(i.get('HIRE_DATE'))
                name = i.get('FIRST_NAME')+''+i.get('LAST_NAME')
                if emp_details.get(hire_date)is None:
                    emp_details.setdefault(hire_date,[name])
                else:
                    emp_details[hire_date].append(name)
        return emp_details


if __name__ == "__main__" :
    obj = HandleCSV()
    # print(obj.read_as_dict())
    print(obj.task_one())
    print(obj.task_two())
