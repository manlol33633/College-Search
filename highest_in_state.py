import csv


def highest_in_state(state):
    
    csv_file = csv.DictReader(open('university-data.csv'))
    highestTuition = 0
    highestUniversity = ""

    for line in csv_file:
        if (line['STABBR'] == state):
            if line['TUITIONFEE_IN'] != '-':
                if (int(line['TUITIONFEE_IN']) > highestTuition):
                    highestTuition = int(line['TUITIONFEE_IN'])
                    highestUniversity = line['INSTNM']
    highest = (highestTuition, highestUniversity)
    return highest