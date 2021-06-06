import os
#Small helper script to insert linebreaks between each entry on map/event files
#Preprocessed so analysis can run as a stream to avoid memory issues
if __name__ == '__main__':

    competitions=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship']
    os.mkdir('../matches_line_breaks')
    os.mkdir('../events_line_breaks')

    for competition in competitions:
        events = open(f'../events/events_{competition}.json','r')
        out = open(f'../events_line_breaks/events_{competition}.json','a')
        indiv_events=events.read()[1:].split('}, {\"eventId')

        for i in range(len(indiv_events)-1):
            out.write(indiv_events[i]+'}\n{\"eventId')

        out.write(indiv_events[len(indiv_events)-1])
        
        out.close()

        matches = open(f'../matches/matches_{competition}.json','r')
        out = open(f'../matches_line_breaks/matches_{competition}.json','a')
        indiv_matches=matches.read()[1:].split('}, {\"status')

        for i in range(len(indiv_matches)-1):
            out.write(indiv_matches[i]+'}\n{\"status')

        out.write(indiv_matches[len(indiv_matches)-1])
        
        out.close()