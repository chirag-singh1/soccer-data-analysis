if __name__ == '__main__':

    players = open('../players.json','r', encoding='utf-8')
    indiv_events=players.read().split('},{')

    for ev in indiv_events:
        if '\"wyId\": 7905' in ev:
            print('{',end='')
            print(ev,end='')
            print('}')
        
    
