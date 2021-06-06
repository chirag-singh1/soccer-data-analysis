import json
import matplotlib.pyplot as plt
import numpy as np
import argparse
from collections import defaultdict

#Helper class to store each goal's set of of information
class Goal:
    def __init__(self,teamId,period,time): #Initialize goal
        self.team=teamId
        self.period=period
        self.time=time
    
    def update_prev_goals(self,team_id1,team_id2,team1_goals,team2_goals): #Update goal with the score before the goal occurred
        self.prev_goals={}
        self.prev_goals[team_id1]=team1_goals
        self.prev_goals[team_id2]=team2_goals
    
#Helper method to update halftime counts 
def update_counts(goal_record, team_1, team_2, half_time_lead_count,half_time_leading_team_win_count,half_time_draw_count,half_time_leading_team_loss_count, winner):
    deficit = goal_record[team_1] - goal_record[team_2] #Calculate deficit and leading team
    if deficit > 0:
        leading_team=team_1
    elif deficit < 0:
        leading_team=team_2
    else:
        leading_team=-1

    half_time_lead_count[abs(deficit)]+=1

    if winner == leading_team: #Assign halftime statistics appropriately
        half_time_leading_team_win_count[abs(deficit)]+=1
    elif int(winner) == 0:
        half_time_draw_count[abs(deficit)]+=1
    elif deficit != 0:
        half_time_leading_team_loss_count[abs(deficit)]+=1
    else:
        half_time_leading_team_loss_count[0]+=1
        half_time_leading_team_win_count[0]+=1

#Main method to parse the goals/match results of a specific competition
def parse_match_results(competition):
    events = open(f'events_line_breaks/events_{competition}.json','r')   
    matches_file = open(f'matches_line_breaks/matches_{competition}.json','r')
    
    goals=defaultdict(list)
    matches={}

    #Initialize matches (including competiting teams and the winner)
    cl=matches_file.readline()
    while(cl):
        curr_line=json.loads(cl)

        matches[curr_line['wyId']]={}
        matches[curr_line['wyId']]['teams']=list(curr_line['teamsData'].keys())
        matches[curr_line['wyId']]['winner']=curr_line['winner']
        
        cl=matches_file.readline()

    #Store each goal in the correct match
    cl=events.readline()
    while(cl):
        curr_line=json.loads(cl)

        if curr_line['eventId'] != 9: #Exclude save attempts that have goal tag
            if sum(1 for x in curr_line['tags']  if x['id']==101) > 0: #Normal goal
                goals[curr_line['matchId']].append(Goal(curr_line['teamId'],curr_line['matchPeriod'],curr_line['eventSec']))
            elif sum(1 for x in curr_line['tags']  if x['id']==102) > 0: #Own goal (swap team)
                team=int(next(x for x in matches[curr_line['matchId']]['teams'] if x != str(curr_line['teamId'])))
                goals[curr_line['matchId']].append(Goal(team,curr_line['matchPeriod'],curr_line['eventSec']))

        cl=events.readline()

    #Initialize metrics for halftime deficit
    half_time_leading_team_win_count=[0]*10
    half_time_leading_team_loss_count=[0]*10
    half_time_draw_count=[0]*10
    half_time_lead_count=[0]*10

    #Loop over matches to fill goalscoring data for each team
    for match in matches.keys():
        goal_record={}
        
        team_1=matches[match]['teams'][0] 
        team_2=matches[match]['teams'][1]
        
        goal_record[team_1]=0
        goal_record[team_2]=0
        
        #Loop over each goal in each match to find the halftime score
        past_half=False
        for goal in goals[match]:
            if not past_half and goal.period !='1H': #First goal past half 
                past_half=True
                update_counts(goal_record, team_1, team_2, half_time_lead_count,half_time_leading_team_win_count,
                half_time_draw_count,half_time_leading_team_loss_count, str(matches[match]['winner']))

            goal.update_prev_goals(team_1,team_2,goal_record[team_1],goal_record[team_2]) #Updates goal objects
            goal_record[str(goal.team)]+=1
        
        if not past_half: #First goal past half 
            update_counts(goal_record, team_1, team_2, half_time_lead_count,half_time_leading_team_win_count,
            half_time_draw_count,half_time_leading_team_loss_count, str(matches[match]['winner']))

    half_time_leading_team_win_count[0]=int(half_time_leading_team_win_count[0]/2) #Corrects for matches tied at halftime
    half_time_leading_team_loss_count[0]=int(half_time_leading_team_loss_count[0]/2)
    loss_base=[a+b for a, b in zip(half_time_leading_team_win_count,half_time_draw_count)]

    return half_time_leading_team_win_count,half_time_draw_count,half_time_leading_team_loss_count,half_time_lead_count, loss_base

if __name__ == '__main__':

    #Setup argument parsing
    parser=argparse.ArgumentParser(description='Generate a variety of graphics centered around the halftime lead of specific games')
    parser.add_argument('-A','--percentage_adjust',required=False,nargs=1, default='False', choices=['True','False'])
    parser.add_argument('-C','--competitions',required=False,nargs='*',default='all',
    choices=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship'])
    args = parser.parse_args()

    #Choose competitions based on arguments
    if args.competitions == 'all':
        competitions=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship']
    else:
        competitions=args.competitions
    
    #Initialize metrics
    half_time_leading_team_win_count=[0]*10
    half_time_draw_count=[0]*10
    half_time_leading_team_loss_count=[0]*10
    half_time_lead_count=[0]*10
    loss_base=[0]*10

    #Loop over competitions, aggregating results for each competition into overall results
    for competition in competitions:
        temp_wins,temp_draws,temp_loss,temp_count,temp_base=parse_match_results(competition)
        loss_base=[a+b for a, b in zip(temp_base,loss_base)]
        half_time_leading_team_win_count=[a+b for a, b in zip(temp_wins,half_time_leading_team_win_count)]
        half_time_draw_count=[a+b for a, b in zip(temp_draws,half_time_draw_count)]
        half_time_leading_team_loss_count=[a+b for a, b in zip(temp_loss,half_time_leading_team_loss_count)]
        half_time_lead_count=[a+b for a, b in zip(temp_count,half_time_lead_count)]
    
    print(half_time_leading_team_win_count)
    print(half_time_draw_count)
    print(half_time_leading_team_loss_count)
    print(half_time_lead_count)

    #Adjust raw win numbers relative to total number if applicable
    if args.percentage_adjust[0]=='True':
        for i in range(10):
            if half_time_lead_count[i] > 0:
                half_time_leading_team_win_count[i]/=half_time_lead_count[i]
                half_time_draw_count[i]/=half_time_lead_count[i]
                half_time_leading_team_loss_count[i]/=half_time_lead_count[i]
                loss_base[i]/=half_time_lead_count[i]

    #Place bars on graph
    x=np.arange(10)
    plt.bar(x, half_time_leading_team_win_count, color='green')
    plt.bar(x, half_time_draw_count, bottom=half_time_leading_team_win_count, color='yellow')
    plt.bar(x, half_time_leading_team_loss_count, bottom=loss_base, color='red')

    #Draw graph with labels/legend/etc.
    plt.legend(labels=['Leading Team Win','Draw','Leading Team Loss'])
    plt.xticks(np.arange(start=0,stop=6))
    plt.xlabel('Halftime Lead')
    plt.ylabel('Result Frequency Percentage')
    plt.title('Final Result Percents by Halftime Lead')
    plt.xlim([-1,6])
    plt.show()