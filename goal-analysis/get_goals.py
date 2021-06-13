import json
import matplotlib.pyplot as plt
import numpy as np

def process_all(match,team,player,goal):
    competitions=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship']
    goal_buildup=[]
    shot_x=[]
    shot_y=[]

    for competition in competitions:
        temp_goal,temp_x,temp_y=process_competition(competition,match,team,player,goal)
        shot_x+=temp_x
        shot_y+=temp_y
        goal_buildup+=temp_goal

    return shot_x,shot_y

def run_analysis(competition,match,team,player,goal,show_buildup):
    if competition == 'all':
        goal_buildup,shot_x, shot_y = process_all(match,team,player,goal)
    else:
        goal_buildup,shot_x,shot_y=process_competition(competition,match,team,player,goal)

    if goal + 1 >= len(shot_x):
        print('Invalid goal selected')
        exit(1)
    elif goal != 0:
        shot_x=shot_x[goal+1]
        shot_y=shot_y[goal+1]
        goal_buildup=goal_buildup[goal+1]

    ax=plt.figure().add_subplot()
    ax.set_aspect(aspect=0.625)

    if show_buildup == 'True':
        if goal == 0:
            print('Cannot show buildup for multiple goals')
            exit(1)

        scoring_team_id=goal_buildup[len(goal_buildup)-1]['teamId']
        for i in range(len(goal_buildup)-1):
            event=goal_buildup[i]
            temp_x=[]
            temp_y=[]
            for pos in event['positions']:
                if scoring_team_id == event['teamId']:
                    temp_y.append(100-pos['y'])
                    temp_x.append(pos['x'])
                else:
                    temp_y.append(pos['y'])
                    temp_x.append(100-pos['x'])
            if event['subEventId'] == 34:
                temp_x[0]=0
                temp_y[0]=50
            
            ax.plot(temp_x,temp_y)
            
            if event['eventId'] == 8:
                slope=(temp_y[1]-temp_y[0])/(temp_x[1]-temp_x[0])
                dx=np.sqrt(0.001**2/(1+slope**2))*(temp_x[1]-temp_x[0])/abs(temp_x[1]-temp_x[0])
                dy=slope*dx
                ax.arrow((temp_x[0]+temp_x[1])/2.0,(temp_y[0]+temp_y[1])/2.0,dx,dy,head_width=1.0,head_length=1.0)

    ax.scatter(shot_x,shot_y)

    center_x1, center_y1 = [50,50],[0,100]
    left_six_box_x,left_six_box_y=[0,6,6,0],[37,37,63,63]
    left_box_x,left_box_y=[0,16,16,0],[19,19,81,81]
    right_six_box_x,right_six_box_y=[100,94,94,100],[37,37,63,63]
    right_box_x,right_box_y=[100,84,84,100],[19,19,81,81]
    ax.plot(center_x1,center_y1, left_six_box_x,left_six_box_y, left_box_x,left_box_y, right_six_box_x,right_six_box_y, right_box_x,right_box_y, color='gray')

    plt.gca().axes.xaxis.set_visible(False)
    plt.gca().axes.yaxis.set_visible(False)
    
    plt.xlim([0,100])
    plt.ylim([0,100])
    plt.show()

def process_competition(competition,match,team,player,goal):

    events = open(f'../events_line_breaks/events_{competition}.json','r')
    cl = events.readline()

    goals=[]
    shot_x=[]
    shot_y=[]

    goal_buildup=[]
    curr_buildup=[]

    while cl:
        curr_line=json.loads(cl)

        if match != 0 and curr_line['matchId'] != match:
            while cl and curr_line['matchId'] != match:
                curr_line=json.loads(cl)
                cl=events.readline()

            curr_buildup=[] 
            if not cl:
                break
        
        if curr_line['eventId'] == 3:
            curr_buildup=[]
        
        if curr_line['eventId'] !=9 or sum(1 for x in curr_line['tags']  if x['id']==101) == 0:
            curr_buildup.append(curr_line)
        
        if curr_line['eventId'] == 2:
            curr_buildup=[]

        if curr_line['eventId'] != 9 and curr_line['subEventName'] != 'Penalty' and sum(1 for x in curr_line['tags']  if x['id']==101) > 0:
            if (player == curr_line['playerId'] or player == 0) and (team == 0 or team == curr_line['teamId']):
                goals.append(curr_line)  
                shot_x.append(curr_line['positions'][0]['x'])
                shot_y.append(100-curr_line['positions'][0]['y'])
                goal_buildup.append(curr_buildup)
            
            curr_buildup=[]

        cl=events.readline()

    if goal == 0:
        for goal in goal_buildup:
            for step in goal:
                print(step)
            print('')
    else:
        if goal + 1 >= len(goal_buildup):
            print('Invalid goal selected')
            exit(1)
        else:
            for step in goal_buildup[goal+1]:
                print(step)

    return goal_buildup,shot_x, shot_y