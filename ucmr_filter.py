import csv
import string
from common import newpathrel

def isEpa537(raw_row):
    'if the MethodID field matches EPA 537'
    return "EPA 537" in raw_row[15]

def detected(raw_row):
    'if the analytical results sign indicates data found over the limit'
    return not "<" in raw_row[16]

def zipForPws(raw_row):
    '''
    given a PWSID in the UCMR3 data,
    use the ZipCodes data to collect all the zips matching that PWS
    '''
    found_zips = []
    with open(newpathrel('ucmr-3-occurrence-data/UCMR3_ZipCodes.txt'), 'rb') as zips_fh:
        reader = csv.reader(zips_fh,  dialect='excel-tab')
        for zip in reader:
            if zip[0] == raw_row[0]:
                'PWSIDs match'
                found_zips.append(zip[1])

    return found_zips

def showSimpleList(xs):
    return string.join(map(str,xs), ', ')


# TODO: use DictReader
# https://docs.python.org/2/library/csv.html#csv.DictReader

if __name__ == '__main__':
    with open(newpathrel('ucmr-3-occurrence-data/UCMR3_All.txt'), 'rb') as ucmr3_filehandle:
        with open('filtered-ucmr3-data.csv', 'wb') as output_filehandle:
            writer = csv.writer(output_filehandle, dialect='excel-tab')
            reader = csv.reader(ucmr3_filehandle,  dialect='excel-tab')

            for ii,row in enumerate(reader):
                if ii == 0:
                    'column headings'
                    row.append('ZipCodes')
                    print row
                    writer.writerow(row)

                if isEpa537(row) and detected(row):
                    # lookup zip codes
                    row.append(showSimpleList(zipForPws(row)))

                    print row
                    writer.writerow(row)

