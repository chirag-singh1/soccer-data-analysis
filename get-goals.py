import json
import matplotlib.pyplot as plt

if __name__ == '__main__':

    events = open('events_line_breaks/events_England.json','r')
    cl = events.readline()

    goals=[]
    shot_x=[]
    shot_y=[]

    goal_buildup=[]
    curr_buildup=[]

    player_id=8717

    while cl:
        curr_line=json.loads(cl)
        
        if curr_line['eventId'] == 3:
            curr_buildup=[]
        
        if curr_line['eventId'] !=9 or sum(1 for x in curr_line['tags']  if x['id']==101) == 0:
            curr_buildup.append(curr_line)
        
        if curr_line['eventId'] == 2:
            curr_buildup=[]

        if curr_line['eventId'] != 9 and curr_line['subEventName'] != 'Penalty' and sum(1 for x in curr_line['tags']  if x['id']==101) > 0:
            if player_id == curr_line['playerId'] or player_id == 0:
                goals.append(curr_line)  
                shot_x.append(curr_line['positions'][0]['x'])
                shot_y.append(100-curr_line['positions'][0]['y'])
                goal_buildup.append(curr_buildup)
            
            curr_buildup=[]

        cl=events.readline()

    for goal in goal_buildup:
        for step in goal:
            print(step)
        print('\n\n')

    ax=plt.figure().add_subplot()
    ax.set_aspect(aspect=0.625)
    
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