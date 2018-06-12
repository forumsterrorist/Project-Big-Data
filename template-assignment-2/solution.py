"""
We truthfully declare:
- to have contributed approximately equally to this assignment [if this is not true, modify this sentence to disclose individual contributions so we can grade accordingly]
- that we have neither helped other students nor received help from other students
- that we provided references for all code that is not our own

Fiachra O Cochlain 2543845@student.vu.nl
Name Student 2 email@vu.nl
"""

def read_csv_data(filenames):
    import pandas as pd
    dataFrame = pd.DataFrame(columns = [
        'bedtime',
        'intended bedtime',
        'rise_time,
        'rise_reason',
        'fitness,
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
                bedtime = inferBedtime(temp[2], temp[3], temp[4])
                

def inferBedtime(userid, time, state):    
    
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





