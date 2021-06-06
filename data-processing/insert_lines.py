if __name__ == '__main__':

    events = open('../events/events_France.json','r')
    out = open('../events_line_breaks/events_France.json','a')
    indiv_events=events.read().split('}, {\"eventId')
    for ev in indiv_events:
        out.write(ev+'}\n{\"eventId')
    
    out.close()