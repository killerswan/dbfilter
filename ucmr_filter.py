import csv
from common import newpathrel

def isEpa537(raw_row):
    'if the MethodID field matches EPA 537'
    return "EPA 537" in raw_row[15]

def detected(raw_row):
    'if the analytical results sign indicates data found over the limit'
    return not "<" in raw_row[16]

if __name__ == '__main__':
    with open(newpathrel('ucmr-3-occurrence-data/UCMR3_All.txt'), 'rb') as ucmr3_filehandle:
        with open('filtered-ucmr3-data.csv', 'wb') as output_filehandle:
            writer = csv.writer(output_filehandle, dialect='excel-tab')
            reader = csv.reader(ucmr3_filehandle,  dialect='excel-tab')

            for row in reader:
                if isEpa537(row) and detected(row):
                    print row
                    writer.writerow(row)

