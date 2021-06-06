import json
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

def parse_matches(competition):
    matches_file = open(f'../matches_line_breaks/matches_{competition}.json','r')
    matches={}
    #Initialize matches (including competiting teams and the winner)
    cl=matches_file.readline()
    while(cl):
        curr_line=json.loads(cl)

        matches[curr_line['wyId']]={}
        matches[curr_line['wyId']]['teams']=list(curr_line['teamsData'].keys())
        matches[curr_line['wyId']]['winner']=curr_line['winner']
        
        cl=matches_file.readline()
    return matches

def parse_goals(competition, matches):
    goals=defaultdict(list)
    events = open(f'../events_line_breaks/events_{competition}.json','r')   

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

    return goals