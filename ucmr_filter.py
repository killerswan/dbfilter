import csv
import string
from common import newpathrel


def isEpa537(raw_row):
    'if the MethodID field matches EPA 537'
    return "EPA 537" in raw_row['MethodID']


def detected(raw_row):
    'if the analytical results sign indicates data found over the limit'
    return not "<" in raw_row['AnalyticalResultsSign']


def zipForPws(raw_row):
    '''
    given a PWSID in the UCMR3 data,
    use the ZipCodes data to collect all the zips matching that PWS
    '''
    found_zips = []
    with open(newpathrel('ucmr-3-occurrence-data/UCMR3_ZipCodes.txt'), 'rb') as zips_fh:
        reader = csv.DictReader(zips_fh,  dialect='excel-tab')
        for zip in reader:
            if zip['PWSID'] == raw_row['PWSID']:
                'PWSIDs match'
                found_zips.append(zip['ZIPCODE'])

    return found_zips


def showSimpleList(xs):
    return string.join(map(str,xs), ', ')


if __name__ == '__main__':
    with open(newpathrel('ucmr-3-occurrence-data/UCMR3_All.txt'), 'rb') as ucmr3_filehandle:
        with open('filtered-ucmr3-data.csv', 'wb') as output_filehandle:
            writer_fieldnames = [
                'PWSID',
                'PWSName',
                'Size',
                'FacilityID',
                'FacilityName',
                'FacilityWaterType',
                'SamplePointID',
                'SamplePointName',
                'SamplePointType',
                'AssociatedFacilityID',
                'AssociatedSamplePointID',
                'CollectionDate',
                'SampleID',
                'Contaminant',
                'MRL',
                'MethodID',
                'AnalyticalResultsSign',
                'AnalyticalResultsValue',
                'SampleEventCode',
                'MonitoringRequirement',
                'Region',
                'State',
                'ZipCodes'
            ]
            writer = csv.DictWriter(output_filehandle, dialect='excel-tab', fieldnames=writer_fieldnames)
            reader = csv.DictReader(ucmr3_filehandle,  dialect='excel-tab')

            for ii,row in enumerate(reader):

                if isEpa537(row) and detected(row):
                    # lookup zip codes
                    row['ZipCodes'] = showSimpleList(zipForPws(row))

                    print row
                    writer.writerow(row)

