"""
We truthfully declare:
- to have contributed approximately equally to this assignment [if this is not true, modify this sentence to disclose individual contributions so we can grade accordingly]
- that we have neither helped other students nor received help from other students
- that we provided references for all code that is not our own
Fiachra O Cochlain 2543845@student.vu.nl
Mark Verheul 2539278@student.vu.nl"""

import datetime

def read_csv_data(filenames):
    import pandas as pd
    dataFrame = pd.DataFrame(columns = [
        'bedtime',
        'intended bedtime',
        'rise_time',
        'rise_reason',
        'fitness',
        'adherence_importance',
        'in_experimental_group'])
        
    for filename in filenames:
        with open(filename) as data:
            bedtime = 0
            intended_bedtime = 0
            rise_time = 0
            rise_reason = 0
            fitness = 0
            adherence_importance = 0
            in_experimental_group = false
            for line in data:
                temp = line.split(';')
                temp_split = temp[2].split('_')
                
                if temp_split[0] == 'lamp' and temp[3] == 'OFF':
                    
                    bedtime = inferBedtime(temp_split)
                    
                elif temp_split[0] == 'nudge':
                    ...
                elif temp_split[0] == 'bedtime':
                elif temp_split[0] == '':
                elif temp_split[0] == '':
                    ...
                    

def inferBedtime(event):    

        
    day = event[2]
    month = get_month(event[3])
    year = event[4]
    hour = event[5]
    minute = event[6]
    second = event[7]
    
    if check_midnight(hour):
        day -= 1
    
    idx = (datetime.datetime(year, month, day, hour, minute, second))
    
    return idx


def check_midnight(hour):
    
    if hour == '00' or hour == '01' or hour == '02' or hour == '03' or hour == '04':
        return True
    else:
        return False
    
def get_month(x):
    
    if x == 'juni':
        return 6
    elif x == 'mei':
        return 5
    elif x == 'augustus':
        return 8
    else:
        print('error')
        
def to_mongodb(df):
    None


def read_mongodb(filter,sort):
    None


if __name__ == '__main__':
    # this code block is run if you run solution.py (instead of run_solution.py)
    # it is convenient for debugging

    df = read_csv_data(["hue_upload.csv","hue_upload2.csv"])
    # to_mongodb(df)
    # read_mongodb({},'_id')



