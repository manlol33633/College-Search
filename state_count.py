import csv
    
def state_count(state):
        csv_file = csv.DictReader(open('university-data.csv'))
        count = 0
        for line in csv_file:
            if(line['STABBR'] == state):
                count += 1
        return count
