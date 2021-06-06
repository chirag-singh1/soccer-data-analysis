import json
import numpy as np
import matplotlib.pyplot as plt

import util

def dist(x1,x2,y1,y2):
    x1*=1.2
    x2*=1.2
    y1*=0.75
    y2*=0.75
    return np.sqrt((x1-x2)**2+(y1-y2)**2)

def parse_passes(competition):
    matches=util.parse_matches(competition)
    events = open(f'../events_line_breaks/events_{competition}.json','r') 

    pass_x_leading=[0]*10
    pass_x_trailing=[0]*10
    pass_dist_leading=[0]*10
    pass_dist_trailing=[0]*10
    pass_count_leading=[0]*10
    pass_count_trailing=[0]*10
    pass_success_leading=[0]*10
    pass_success_trailing=[0]*10

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
            pos=curr_event['positions']
            if goal_record[str(curr_event['teamId'])] > goal_record[str(next(x for x in matches[curr_match]['teams'] if str(x) != str(curr_event['teamId'])))]:
                pass_x_leading[deficit]+=pos[0]['x']
                pass_count_leading[deficit]+=1
                if len(pos) > 1:
                    pass_dist_leading[deficit]+=dist(pos[0]['x'],pos[1]['x'],pos[0]['y'],pos[1]['y'])
                if sum(1 for x in curr_event['tags'] if x['id'] == 1801):
                    pass_success_leading[deficit]+=1                    
            elif deficit == 0:
                pass_x_leading[0]+=pos[0]['x']
                pass_x_trailing[0]+=pos[0]['x']
                if len(pos) > 1:
                    pass_dist_leading[0]+=dist(pos[0]['x'],pos[1]['x'],pos[0]['y'],pos[1]['y'])
                pass_count_leading[0]+=1
                pass_count_trailing[0]+=1
                if sum(1 for x in curr_event['tags'] if x['id'] == 1801):
                    pass_success_leading[deficit]+=1  
                    pass_success_trailing[deficit]+=1
            else:  
                pass_x_trailing[deficit]+=pos[0]['x']
                if len(pos) > 1:
                    pass_dist_trailing[deficit]+=dist(pos[0]['x'],pos[1]['x'],pos[0]['y'],pos[1]['y'])
                pass_count_trailing[deficit]+=1
                if sum(1 for x in curr_event['tags'] if x['id'] == 1801):
                    pass_success_trailing[deficit]+=1  
        
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
    pass_dist_leading[0]/=2
    pass_dist_trailing[0]=pass_dist_leading[0]
    pass_success_leading[0]/=2
    pass_success_trailing[0]/=2
    
    return pass_x_leading,pass_x_trailing,pass_count_leading,pass_count_trailing, pass_dist_leading,pass_dist_trailing, pass_success_leading,pass_success_trailing

def run_analysis(competitions, mode):
    pass_x_leading=[0]*10
    pass_x_trailing=[0]*10
    pass_count_leading=[0]*10
    pass_count_trailing=[0]*10
    pass_dist_leading=[0]*10
    pass_dist_trailing=[0]*10
    pass_success_trailing=[0]*10
    pass_success_leading=[0]*10

    for competition in competitions:
        temp_x_l,temp_x_t,temp_count_l,temp_count_t,temp_dist_l,temp_dist_t,temp_success_l,temp_success_t=parse_passes(competition)
        pass_x_leading=[a+b for a, b in zip(temp_x_l,pass_x_leading)]    
        pass_x_trailing=[a+b for a, b in zip(temp_x_t,pass_x_trailing)]        
        pass_count_leading=[a+b for a, b in zip(temp_count_l,pass_count_leading)]        
        pass_count_trailing=[a+b for a, b in zip(temp_count_t,pass_count_trailing)]
        pass_dist_leading=[a+b for a, b in zip(temp_dist_l,pass_dist_leading)]
        pass_dist_trailing=[a+b for a, b in zip(temp_dist_t,pass_dist_trailing)]
        pass_success_trailing=[a+b for a, b in zip(temp_success_t,pass_success_trailing)]
        pass_success_leading=[a+b for a, b in zip(temp_success_l,pass_success_leading)]

        

    for i in range(10):
        if pass_count_leading[i] > 0:
            pass_x_leading[i]/=pass_count_leading[i]
            pass_dist_leading[i]/=pass_count_leading[i]
            pass_success_leading[i]/=pass_count_leading[i]

        if pass_count_trailing[i] > 0:
            pass_x_trailing[i]/=pass_count_trailing[i]
            pass_dist_trailing[i]/=pass_count_trailing[i]
            pass_success_trailing[i]/=pass_count_trailing[i]

    if mode == 'Location':
        print(pass_x_leading)
        print(pass_x_trailing)

        x=np.arange(0,10)
        plt.plot(x,pass_x_leading,color='green')
        plt.plot(x,pass_x_trailing,color='red')

        plt.xlabel('Lead (Goals)')
        plt.ylabel('Average Pass Start Location (as percent of field)')
        plt.xlim([0,8])
        plt.ylim([30,70])
        plt.title('Pass Locations by Lead')
        plt.legend(labels=['Leading Team','Trailing Team'])
        plt.show()
    
    if mode == 'Accuracy':
        print(pass_success_trailing)
        print(pass_success_leading)

        x=np.arange(0,10)
        plt.plot(x,pass_success_leading,color='green')
        plt.plot(x,pass_success_trailing,color='red')

        plt.xlabel('Lead (Goals)')
        plt.ylabel('Pass Accuracy')
        plt.xlim([0,8])
        plt.ylim([0,1])
        plt.title('Pass Accuracy by Lead')
        plt.legend(labels=['Leading Team','Trailing Team'])
        plt.show()

    if mode == 'Distance':
        print(pass_dist_leading)
        print(pass_dist_trailing)

        x=np.arange(0,10)
        plt.plot(x,pass_dist_leading,color='green')
        plt.plot(x,pass_dist_trailing,color='red')

        plt.xlabel('Lead (Goals)')
        plt.ylabel('Average Pass Distance (yds)')
        plt.xlim([0,8])
        plt.ylim([15,30])
        plt.title('Pass Distance by Lead')
        plt.legend(labels=['Leading Team','Trailing Team'])
        plt.show()