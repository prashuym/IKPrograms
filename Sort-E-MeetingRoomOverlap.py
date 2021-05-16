"""
252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [ [s1, e1],[s2,e2],.... ] (Si > Ei), determine if a person could attend all meetings.
Example1 :
Input : [ [0,30], [5,10], [15,20] ]
Output : False

Input : [ [7,10], [2,4], [15,20] ]
Output : True
"""

def findMeetingOverlap (schedule):
    schedule.sort(key=lambda r: r[0])
    i = 0
    len_schedule = len(schedule)
    print (schedule)
    while i < len_schedule-1 :
        print (schedule[i][1] , schedule[i+1][0])
        if schedule[i][1] > schedule[i+1][0] : return False
        i += 1

    return True

if __name__ == "__main__" :
    schedule = [ [0,30], [35,40], [35,40] ]
    #schedule = [ [7,10], [2,4], [15,20] ]
    print (findMeetingOverlap(schedule))