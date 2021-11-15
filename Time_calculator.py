def add_time(start, duration, Day=False):
        
        #splits start time 
    start_min=int(start.split(':')[1].split(' ')[0]) #splits the min AM/PM into (min, AM/PM) and select min
    start_hr=int(start.split(':')[0])                # selects the hr
    
    duration_split=duration.split(':')  # splits time into hr,min
    duration_hr=int(duration_split[0])
    dur_min=int(duration_split[1])
    
    Days_of_week={'sunday':0, "monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5,"saturday":6}
    Days_list=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    
    am_pm=start.split(':')[1].split(' ')[1]      # selects the AM/PM 
    am_pm_flip={"AM":"PM","PM":"AM"}

    end_mins=start_min+dur_min
    
    if end_mins>59:  # if mins is 60 or  more,
        start_hr+=1     # adds 1 per 60 min increment. Can rewrite as start_hr + int(end_mins % 60)
        end_mins=end_mins%60    # remainder
    no_of_am_pm_flips=int((start_hr+duration_hr)/12)    #no of flips of am or pm per 12 hrs
    end_hr=(start_hr+duration_hr)%12    # final hr time
    
    Days_dur=int(duration_hr/24)
    
    end_mins=end_mins if end_mins>9 else '0'+str(end_mins) #Condition attached to the variable
    end_hr=end_hr =12 if end_hr==0 else end_hr  # LEARN TERNARY OPERATOR
    
    if (am_pm=="PM" and start_hr+(duration_hr%12)>=12): 
        Days_dur+=1
# We're saying that if start dur == PM , the remaider of the dur when added to the start hr should be less
# than 12. If 12 or more, it means another day has approached. Eg 11:59 PM + 72:03 would give
# 12+ (12 + 12 + 12 + 12 + 12 + 12 )
# AM   PM   AM  PM    AM    PM  AM  ------gives 3 Days_of_week later 12:02 AM
    am_pm=am_pm_flip[am_pm] if no_of_am_pm_flips % 2==1 else am_pm
    '''
    The code above means that, depending on the index(key), if the no of flips(the no of 12 hrs that passed)
    is 1 (i.e. odd, which means its now 12 hrs), the key flips.

    if am_pm was am and the no of flips%2 ==1, it implies that am_pm['AM'] will return a value of "PM".
    if the no of flips %2 == 0, the same key will be maintained
    '''
    Calc_time=str(end_hr)+':'+str(end_mins)+' '+am_pm
        
    if Day:
        Day=Day.lower() #Converts imput argument(i.e. optional parameter) to lowercase
        Day_index=int((Days_of_week[Day]+Days_dur))%7 # Days_of_week in a week. the remainder infers to a new week
        # finds the val of the key(i.e. val of the day typed) and adds it to the Days dur and find the remainder
       
        new_day= Days_list[Day_index] # based on the rem, a new val that matches Day will be used
        Calc_time+= ', '+new_day     # New time(ln 46) + , + new_day obtained


    if Days_dur==1:
        return  Calc_time + ' ' + '(next day)'
    elif Days_dur>1:
        return Calc_time + ' (' + str(Days_dur) + ' days later)'

    return Calc_time 


