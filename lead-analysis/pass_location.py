import json
import util
def parse_passes(competition):
    matches=util.parse_matches(competition)
    events = open(f'../events_line_breaks/events_{competition}.json','r') 

    pass_x_leading=[0]*10
    pass_x_trailing=[0]*10
    pass_count_leading=[0]*10
    pass_count_trailing=[0]*10

    goal_record={}
    curr_match=0
    team_1=0
    team_2=0

    cl=events.readline()
    while(cl):
        curr_event=json.loads(cl)

        if curr_event['matchId'] != curr_match: #Start of new match
            #Reset state variables
            curr_match=curr_event['matchId']
            goal_record={}
            team_1=matches[curr_match]['teams'][0] 
            team_2=matches[curr_match]['teams'][1]
            goal_record[team_1]=0
            goal_record[team_2]=0
        
        if curr_event['eventId'] == 8:
            deficit=abs(goal_record[team_1]-goal_record[team_2])
            if goal_record[str(curr_event['teamId'])] > goal_record[str(next(x for x in matches[curr_match]['teams'] if str(x) != str(curr_event['teamId'])))]:
                pass_x_leading[deficit]+=curr_event['positions'][0]['x']
                pass_count_leading[deficit]+=1
            elif deficit == 0:
                pass_x_leading[0]+=curr_event['positions'][0]['x']
                pass_x_trailing[0]+=curr_event['positions'][0]['x']
                pass_count_leading[0]+=1
                pass_count_trailing[0]+=1
            else:  
                pass_x_trailing[deficit]+=curr_event['positions'][0]['x']
                pass_count_trailing[deficit]+=1
        
        if curr_event['eventId'] != 9: #Exclude save attempts that have goal tag
            if sum(1 for x in curr_event['tags']  if x['id']==101) > 0: #Normal goal
                goal_record[str(curr_event['teamId'])]+=1
            elif sum(1 for x in curr_event['tags']  if x['id']==102) > 0: #Own goal (swap team)
                goal_record[str(next(x for x in matches[curr_event['matchId']]['teams'] if x != str(curr_event['teamId'])))]+=1
                

        cl=events.readline()

    pass_x_leading[0]/=2
    pass_x_trailing[0]/=2
    pass_count_trailing[0]/=2
    pass_count_leading[0]/=2

    return pass_x_leading,pass_x_trailing,pass_count_leading,pass_count_trailing

def run_analysis(competitions):
    pass_x_leading=[0]*10
    pass_x_trailing=[0]*10
    pass_count_leading=[0]*10
    pass_count_trailing=[0]*10

    for competition in competitions:
        temp_x_l,temp_x_t,temp_count_l,temp_count_t=parse_passes(competition)
        pass_x_leading=[a+b for a, b in zip(temp_x_l,pass_x_leading)]    
        pass_x_trailing=[a+b for a, b in zip(temp_x_t,pass_x_trailing)]        
        pass_count_leading=[a+b for a, b in zip(temp_count_l,pass_count_leading)]        
        pass_count_trailing=[a+b for a, b in zip(temp_count_t,pass_count_trailing)]

    for i in range(10):
        if pass_count_leading[i] > 0:
            pass_x_leading[i]/=pass_count_leading[i]
        if pass_count_trailing[i] > 0:
            pass_x_trailing[i]/=pass_count_trailing[i]
    
    print(pass_x_leading)
    print(pass_x_trailing)
    print(pass_count_leading)
    print(pass_count_trailing)