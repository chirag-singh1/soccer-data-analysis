import matplotlib.pyplot as plt
import numpy as np
import util

def parse_match_records(competition):
    matches=util.parse_matches(competition)
    goals=util.parse_goals(competition, matches)

    leading_scores_next=[0]*10
    trailing_scores_next=[0]*10
    no_score_next=[0]*10

    for match in matches.keys():
        goal_record={}
        
        team_1=matches[match]['teams'][0] 
        team_2=matches[match]['teams'][1]
        
        goal_record[team_1]=0
        goal_record[team_2]=0

        for goal in goals[match]:
            deficit = abs(goal_record[team_1] - goal_record[team_2])

            if goal_record[team_1] > goal_record[team_2]:
                if str(goal.team) == team_1:
                    leading_scores_next[deficit]+=1
                else:
                    trailing_scores_next[deficit]+=1
            elif goal_record[team_1] < goal_record[team_2]:
                if str(goal.team) == team_2:
                    leading_scores_next[deficit]+=1
                else:
                    trailing_scores_next[deficit]+=1
            else:
                leading_scores_next[deficit]+=1
                trailing_scores_next[deficit]+=1

            goal_record[str(goal.team)]+=1
        
        no_score_next[abs(goal_record[team_1] - goal_record[team_2])]+=1
    
    leading_scores_next[0]=int(leading_scores_next[0]/2) #Corrects for matches tied at halftime
    trailing_scores_next[0]=int(trailing_scores_next[0]/2)

    return leading_scores_next,trailing_scores_next,no_score_next

def run_analysis(competitions, percent_adjust):
    leading_scores_next=[0]*10
    trailing_scores_next=[0]*10
    no_score_next=[0]*10

    for competition in competitions:
        lead,trail,none=parse_match_records(competition)
        leading_scores_next=[a+b for a, b in zip(lead,leading_scores_next)]
        trailing_scores_next=[a+b for a, b in zip(trail,trailing_scores_next)]
        no_score_next=[a+b for a, b in zip(none,no_score_next)]

    print(leading_scores_next)
    print(trailing_scores_next)
    print(no_score_next)

    base=[a+b for a, b in zip(trailing_scores_next,no_score_next)]

    if percent_adjust:
        tot_goals=[a+b+c for a, b, c in zip(leading_scores_next,trailing_scores_next,no_score_next)]
        for i in range(10):
            if tot_goals[i] > 0:
                leading_scores_next[i]/=tot_goals[i]
                trailing_scores_next[i]/=tot_goals[i]
                no_score_next[i]/=tot_goals[i]
                base[i]/=tot_goals[i]

    x=np.arange(10)

    plt.plot(x,trailing_scores_next, color='red')
    plt.plot(x,no_score_next, color='orange')
    plt.plot(x,leading_scores_next, color='green')

    plt.legend(labels=['Trailing Team Scores Next','No Further Goals','Leading Team Scores Next'])
    plt.xticks(np.arange(start=0,stop=9))
    plt.xlim([0,8])
    plt.xlabel('Goal Deficit')
    
    if percent_adjust:
        plt.ylabel('Next Scorer Probability')
        plt.title('Next Scorer Probability by Goal Deficit')
    else:
        plt.ylabel('Next Scorer')
        plt.title('Next Scorer by Goal Deficit')

    plt.show()