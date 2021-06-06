import matplotlib.pyplot as plt
import numpy as np
import json
import util

def get_shots_for_competition(competition):
    matches=util.parse_matches(competition)
    events = open(f'../events_line_breaks/events_{competition}.json','r') 

    curr_match=0  
    start_sec=0
    team_1=0
    team_2=0
    leading_team=0
    shots_leading=[0]*10
    shots_trailing=[0]*10  
    sec_deficit=[0]*10
    goal_record={}
    curr_period=''
    prev_sec=0
    sec_offset=0

    cl=events.readline()
    while(cl):
        curr_event=json.loads(cl)

        if curr_event['matchPeriod'] == 'P':
            while('\"matchPeriod\": \"P\"' in cl):
                cl=events.readline()
            curr_event=json.loads(cl)
    
        if curr_event['matchId'] != curr_match:
            if curr_match != 0:
                sec_deficit[abs(goal_record[team_1]-goal_record[team_2])]+=(prev_sec+sec_offset)-start_sec
    
            curr_match=curr_event['matchId']
            goal_record={}
            team_1=matches[curr_match]['teams'][0] 
            team_2=matches[curr_match]['teams'][1]
        
            goal_record[team_1]=0
            goal_record[team_2]=0
            start_sec=0
            sec_offset=0
            prev_sec=0
            leading_team=0
            curr_period=curr_event['matchPeriod']
        
        if curr_period != curr_event['matchPeriod']:
            curr_period=curr_event['matchPeriod']
            sec_offset+=prev_sec

        if curr_event['eventId'] == 10 or curr_event['subEventId'] == 33 or curr_event['subEventId'] == 35:
            if str(curr_event['teamId']) == str(leading_team):
                shots_leading[abs(goal_record[team_1]-goal_record[team_2])]+=1
            elif leading_team == 0:
                shots_leading[0]+=1
                shots_trailing[0]+=1
            else:
                shots_trailing[abs(goal_record[team_1]-goal_record[team_2])]+=1
        
        if curr_event['eventId'] != 9: #Exclude save attempts that have goal tag
            if sum(1 for x in curr_event['tags']  if x['id']==101) > 0: #Normal goal
                sec_deficit[abs(goal_record[team_1]-goal_record[team_2])]+=(curr_event['eventSec']+sec_offset)-start_sec
                goal_record[str(curr_event['teamId'])]+=1
                if goal_record[team_1] > goal_record[team_2]:
                    leading_team=team_1
                elif goal_record[team_2] > goal_record[team_1]:
                    leading_team=team_2
                else:
                    leading_team = 0
                start_sec = curr_event['eventSec']+sec_offset
            elif sum(1 for x in curr_event['tags']  if x['id']==102) > 0: #Own goal (swap team)
                team=int(next(x for x in matches[curr_event['matchId']]['teams'] if x != str(curr_event['teamId'])))
                sec_deficit[abs(goal_record[team_1]-goal_record[team_2])]+=(curr_event['eventSec']+sec_offset)-start_sec
                goal_record[str(team)]+=1
                if goal_record[team_1] > goal_record[team_2]:
                    leading_team=team_1
                elif goal_record[team_2] > goal_record[team_1]:
                    leading_team=team_2
                else:
                    leading_team = 0
                start_sec = curr_event['eventSec']+sec_offset

        prev_sec=curr_event['eventSec']
        cl=events.readline()

    shots_leading[0]/=2
    shots_trailing[0]/=2
    
    return shots_leading,shots_trailing, sec_deficit

def run_analysis(competitions):
    shots_per_min_leading=[0]*10
    shots_per_min_trailing=[0]*10
    sec_deficit=[0]*10

    for competition in competitions:
        temp_lead,temp_trail,temp_deficit=get_shots_for_competition(competition)
        shots_per_min_leading=[a+b for a, b in zip(shots_per_min_leading,temp_lead)]
        shots_per_min_trailing=[a+b for a, b in zip(shots_per_min_trailing,temp_trail)]
        sec_deficit=[a+b for a, b in zip(sec_deficit,temp_deficit)]

    for i in range(10):
        if sec_deficit[i] > 0:
            shots_per_min_leading[i]/=(sec_deficit[i]/60.0)
            shots_per_min_trailing[i]/=(sec_deficit[i]/60.0)

    print(shots_per_min_leading)
    print(shots_per_min_trailing)

    x=np.arange(10)

    plt.plot(x,shots_per_min_leading, color='green')
    plt.plot(x,shots_per_min_trailing, color='red')
    plt.show()