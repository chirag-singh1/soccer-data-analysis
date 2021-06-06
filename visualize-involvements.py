import json
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    events = open('events_line_breaks/events_England.json','r')
    cl = events.readline()

    actions=[]
    action_x=[]
    action_y=[]

    player_id=8717
    #3353- iniesta
    #20475-vidal
    #3476-rakitic
    #3346- sergio busquest
    #3359 - messi
    #7910 - de gea
    #8717 -kane
    #167145 -bellerin
    #31528 -kante
    #8643 -lowton
    while cl:
        curr_line=json.loads(cl)

        if player_id == curr_line['playerId'] or player_id == 0:
            actions.append(curr_line)  
            action_x.append(curr_line['positions'][0]['x'])
            action_y.append(100-curr_line['positions'][0]['y'])
            
        cl=events.readline()
            
    print(actions)

    ax=plt.figure().add_subplot()
    ax.set_aspect(aspect=0.625)

    locations=np.zeros((26,26))
    for i in range (len(action_x)):
        locations[int(action_y[i]/4)][int(action_x[i]/4)]+=1
    
    locations_extended=np.zeros((101,101))
    for i in range(101):
        for j in range(101):
            locations_extended[i][j]=locations[int(i/4)][int(j/4)]

    ax.imshow(locations_extended, cmap='viridis', interpolation='none', aspect=0.625)
    #ax.scatter(action_x,action_y)

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