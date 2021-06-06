import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

if __name__ == '__main__':

    targetTeamId=676
    matchId=2565884

    events = open('events_line_breaks/events_Spain.json','r')
    matches = open('matches_line_breaks/matches_Spain.json','r', encoding='utf-8')

    players=set()
    player_x=defaultdict(int)
    player_y=defaultdict(int)
    player_count=defaultdict(int)
    player_index_dict={}

    cl=matches.readline()

    while(cl):
        curr_line=json.loads(cl)

        if curr_line['wyId'] == matchId:
            for player in curr_line['teamsData'][str(targetTeamId)]['formation']['lineup']:
                players.add(player['playerId'])

        cl=matches.readline()

    cl = events.readline()

    while cl:
        curr_line=json.loads(cl)

        if curr_line['teamId']==targetTeamId and (matchId == 0 or matchId == curr_line['matchId']) and curr_line['playerId'] in players:
            player_x[curr_line['playerId']]+=curr_line['positions'][0]['x']
            player_y[curr_line['playerId']]+=(100-curr_line['positions'][0]['y'])
            player_count[curr_line['playerId']]+=1
        
        cl = events.readline()

    for i in player_count.keys():
        if player_count[i]>0:
            player_x[i]/=player_count[i]
            player_y[i]/=player_count[i]
    

    players_file = open('players.json','r', encoding='utf-8')
    cl = players_file.readline()

    while(cl):
        curr_line=json.loads(cl)

        if(curr_line['wyId'] in players):
            player_index_dict[curr_line['wyId']]=curr_line['label']

        cl = players_file.readline() 

    fig, ax=plt.subplots()
    ax.set_aspect(aspect=0.625)
    ax.scatter(player_x.values(),player_y.values())

    for val in player_index_dict.keys():
       ax.annotate(player_index_dict[val],(player_x[val],player_y[val]))

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
        