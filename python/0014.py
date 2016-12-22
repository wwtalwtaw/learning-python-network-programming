# -*- coding=utf-8 -*-

import re
from xlwt import Workbook
from xlwt import Worksheet

class solution0014(object):
    def __init__(self,filename):
        fileobj = open(filename)
        self.content = fileobj.read()
        self.pattern = re.compile('"(.*)":\["(.*)",(.*),(.*),(.*)\]')
        self.data = []

    def get_data(self):
        self.data = re.findall(self.pattern,self.content)

    def write_data(self):
        book = Workbook(encoding='utf-8')
        sheet = book.add_sheet(sheetname='1',cell_overwrite_ok=True)
        row = 0
        for line in self.data:
            for col in range(len(line)):
                sheet.write(row,col,line[col])
            row += 1
        book.save('student.xls')

    def show(self):
        print self.content

so = solution0014("student.txt")
so.get_data()
so.show()
so.write_data()