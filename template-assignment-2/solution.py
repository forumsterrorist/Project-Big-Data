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
        
    entries = []
    experimental_group_members = []
        
    for filename in filenames:
        with open(filename) as data:
            bedtime = 0
            intended_bedtime = 0
            rise_time = 0
            rise_reason = 0
            fitness = 0
            adherence_importance = 0
            in_experimental_group = false
            date = 0
            uid = 0
            for line in data:
                temp = line.split(';')
                temp_split = temp[2].split('_')
                
                uid = temp[1]
                
                if experimental_group_members.contains(uid)
                    in_experimental_group = true
                else:
                    in_experimental_group = false
                
                if temp_split[0] == 'lamp' and temp[3] == 'OFF':
                    bedtime = inferBedtime(temp_split)
                elif temp_split[4] == 'nudge':
                    in_experimental_group = true
                    experimental_group_members.append = uid
                elif temp_split[4] == 'bedtime':
                    day = temp_split[1]
                    month = get_month(temp_split[2])
                    year = temp_split[3]
                    hour = temp[3][0:1]
                    minute = temp[3][2:3]
                    second = 00
                    intended_bedtime, date = (datetime.datetime(year, month, day, hour, minute, second))
                elif temp_split[4] == 'risetime':
                    day = temp_split[1]
                    month = get_month(temp_split[2])
                    year = temp_split[3]
                    hour = temp[3][0:1]
                    minute = temp[3][2:3]
                    second = 00
                    rise_time, date = (datetime.datetime(year, month, day, hour, minute, second))
                elif temp_split[4] == 'rise':
                    rise_reason = temp[3]
                elif temp_split[4] == 'fitness':
                    fitness = temp[3]
                elif temp_split[4] == 'adherence_importance':
                    adherence_importance = temp[3]
                else
                    pass
            
                idx = (date, uid)
                entry = pd.Series([bedtime, intended_bedtime, rise_time, rise_reason, fitness, adherence_importance, in_experimental_group], index = [idx])
                entries.append(entry)

    for entry in entries:
        dataFrame = dataFrame.concat(dataFrame, entry)
                    

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

def insert_if_new(df,idx):
    if idx not in df.index:
        df = df.append(pd.Series({'bedtime' : float('nan'), 'intended bedtime' : float('nan'), 'risetime' : float('nan'), 'rise reason' : float('nan'),  'fitness' : float('nan'),'adherence importance' : float('nan'),  'in experimental group' : False}, name=idx))
    return df

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



