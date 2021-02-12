import os
import sys
import json
import pandas as pd
# from pyfiglet import Figlet

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
text = ""
result_label = "Patient: Fast Progressor :{f_progressor}, UMN Problems :{umn_porblems}"

# print("------------")
# print(iexec_out)
# print(iexec_in)
# print(os.path.exists(iexec_in + '/test_patient_data.csv'))
# print(os.listdir(iexec_in))

# this function takes a dataframe of a patient and returns whether she is a slow progressor or a fast progressor
def is_fast_progressor(df):
    # this here is a very simple exmample
    # we classify everybody as a fast progressor who drops more than -1 for question P10 within one month
    # the dataframe needs to be ordered by months
    patient = pd.DataFrame(df)
    patient['lastMonthP10'] = patient['P10'].shift(1)
    patient['diffP10'] = patient['lastMonthP10'] - patient['P10']
    for index, row in patient.iterrows():
        if(row['diffP10'] > 1):
            print("Fast Progressor")
            return True
    print("Slow Progressor")
    return False


# takes a dataframe of a patient and returns whether has UMN problems or not
def has_UMN_problems(df):
    patient = pd.DataFrame(df)
    for index, row in patient.iterrows():
        if(row['UMN'] > 0):
            print("Has UMN Problems")
            return True
    print("Has no UMN Problems")
    return False

#APP Logic
# Use some confidential assets
if os.path.exists(iexec_in + '/test_patient_data.csv'):

    print("start pulling data")
    patient = pd.read_csv(iexec_in + "/test_patient_data.csv")
    is_fast_progressor(patient)
    has_UMN_problems(patient)
    text = result_label.format(f_progressor = is_fast_progressor(patient), umn_porblems = has_UMN_problems(patient))

# Append some results
with open(iexec_out + '/result.txt', 'w+') as f:
    f.write(text)

# Declare everything is computed
with open(iexec_out + '/computed.json', 'w+') as f:
    json.dump({ "deterministic-output-path" : iexec_out + '/result.txt' }, f)
