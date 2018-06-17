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
            uid = 0
            date = pd.datetime.datetime
            for line in data:
                temp = line.split(';')
                uid = temp[1]
                event = temp[2].split('_')
                if event [4] == "bedtime":
                    intended_bedtime = inferBedtime (event[0], event[1], event[2], event[3])
                else if event[4] = "fitness":
                    fitness = temp[3]
                    
                else if event[4] = "adherence":
                    adherence_importance = temp[3]
                bedtime = inferBedtime(temp[1], temp[2], temp[3])
                

def inferBedtime(userid, time, state):    

    
    time_split = time.split('_')
    day = time_split[3]
    month = get_month(time_split[4])
    year = time_split[5]
    hour = time_split[6]
    minute = time_split[7]
    second = time_split[8]
    
    idx = (datetime.datetime(year, month, day, hour, minute, second))
    return idx


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



