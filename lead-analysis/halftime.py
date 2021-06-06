from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import util
    
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
    matches=util.parse_matches(competition)
    goals=util.parse_goals(competition, matches)
    
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

#Main driver to aggregate results over all competitions and display graph
def run_analysis(competitions, percentage_adjust):
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
    if percentage_adjust=='True':
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