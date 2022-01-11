"""
Are there differences in activity patterns between weekdays and weekends?
1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a 
given date is a weekday or weekend day.
2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps 
taken, averaged across all weekdays or weekend days (y-axis).
"""
import csv
import matplotlib.pyplot as plt
import datetime as dt
import pygal
import statistics as st
from datetime import datetime

filename = 'activity.csv'

dictDate = {}
dictInterval = {}

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow)

    for row in reader:
        steps = row[0]
        #disregard NA values
        if steps!= 'NA':
            date = row[1]
            date2 = int(dt.datetime.strptime(date,'%Y-%m-%d').day)
            
            interval = int(row[2])
            
            #populate the dictionary
            #if the date exists, nothing happense
            #otherwise, add new key in the dictionary
            dictDate.setdefault(str(date),[])
            #populate the list with the number of steps
            #taken in the specific date
            dictDate[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
            
    listDate = []   #store the dates
    listSteps = []  #stores the total number of steps taken per day
    listAve = []     #stores the average number of steps taken per day

    for i in dictDate.keys():
        listDate.append(i)
        listSteps.append(sum(dictDate.get(i)))
        listAve.append(st.mean(dictDate.get(i)))


    listWeek = []    #stores the weekday/weekend

    listStepWeekend = []    #stores the steps on weekend on that interval
    listStepWeekday = []    #stores the steps on weekday on that interval

    listAvgWeekend = []     #stores the average number of steps on weekend on that interval
    listAvgWeekday = []     #stores the average number of steps on weekday on that interval
    
    #list of weekdays/weekends to compare with the date for to sort out which is which
    Date_List = ['{}{}{}'.format(y,m,d) for y, m, d in map(lambda x: str(x).split('-'), listDate)]
    for i in range(len(Date_List)):
        dates = Date_List[i]           
        year = int(str(dates[0])+str(dates[1])+str(dates[2])+str(dates[3]))
        month = int(str(dates[4])+str(dates[5]))
        day = int(str(dates[6])+str(dates[7]))
        d = datetime(year, month, day)
        if d.weekday() > 4:
            listWeek.append('weekend')
        else:
            listWeek.append('weekday')
    
    listInterval= list(dictInterval.keys())    #List of the intervals 0-2355

    nums = 0
    for i in range(len(listInterval)):
        listStep = dictInterval.get(listInterval[nums])

        for i in range(len(listStep)):
            listStepIntervalsend=[]
            listStepIntervalsday=[]
            #separating the weekend and weekday steps
            num = 0
            for i in range(len(listWeek)):
                if listWeek[num] == 'weekend':
                    listStepIntervalsend.append(listStep[num])
                else:
                    listStepIntervalsday.append(listStep[num])
                num += 1
            listStepWeekend.append(listStepIntervalsend)
            listStepWeekday.append(listStepIntervalsday)
        nums +=1
    #something's already weird with the list

    #Getting the avg
    numss = 0
    for i in listStepWeekend:
        listAvgWeekend.append(st.mean(listStepIntervalsend[numss]))
        numss += 1
    numsss = 0
    for i in listAvgWeekday:
        listAvgWeekday.append(st.mean(listStepIntervalsday[numsss]))
        numsss += 1

    hist = pygal.Bar()
    hist.title = "Weekend"
    hist.x_title = "Interval"
    hist.y_title = "Steps per Day"
    hist.x_labels = listStep
    hist.add("Average Step",listAvgWeekend)
    hist.render_to_file('weekend.svg')

    hist = pygal.Bar()
    hist.title = "Weekend"
    hist.x_title = "Interval"
    hist.y_title = "Steps per Day"
    hist.x_labels = listStep
    hist.add("Average Step",listAvgWeekend)
    hist.render_to_file('weekday.svg')
