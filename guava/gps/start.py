
# code from https://maxcandocia.com library from http://dtcooper.github.io/python-fitparse/
"""
place this file inside of the directory containing the .fit files and execute it with python3
to execute it from another directory, use
os.chdir('/.../directory_with_fit_files/')
os.system('python3 convert_fit_to_csv.py')
toggle ALT_FILENAME to change naming scheme
currently recommended to keep at =True, since event type is placed in filename
of created objects
"""

import csv
import os
# to install fitparse, run
# sudo pip3 install -e git+https://github.com/dtcooper/python-fitparse#egg=python-fitparse
import fitparse
import pytz

allowed_fields = ['timestamp', 'position_lat', 'position_long', 'distance',
                  'enhanced_altitude', 'altitude', 'enhanced_speed',
                  'speed', 'heart_rate', 'cadence', 'fractional_cadence']
required_fields = ['timestamp', 'position_lat', 'position_long', 'altitude']

UTC = pytz.UTC
CST = pytz.timezone('US/Central')


def main(file):
    new_filename = file[:-4] + '.csv'
    fitfile = fitparse.FitFile(
        file, data_processor=fitparse.StandardUnitsDataProcessor())

    print('converting %s' % file)
    filefile = write_fitfile_to_csv(fitfile, new_filename)
    print('finished conversions')
    return filefile


def write_fitfile_to_csv(fitfile, output_file='test_output.csv'):
    messages = fitfile.messages
    data = []
    for m in messages:
        skip = False
        if not hasattr(m, 'fields'):
            continue
        fields = m.fields
        # check for important data types
        mdata = {}
        for field in fields:
            if field.name in allowed_fields:
                if field.name == 'timestamp':
                    mdata[field.name] = UTC.localize(
                        field.value).astimezone(CST)
                else:
                    mdata[field.name] = field.value
        for rf in required_fields:
            if rf not in mdata:
                skip = False
        if not skip:
            data.append(mdata)
    # write to csv
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(allowed_fields)
        for entry in data:
            writer.writerow([str(entry.get(k, '')) for k in allowed_fields])
    print('wrote %s' % output_file)
    return output_file
