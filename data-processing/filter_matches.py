import json

if __name__ == '__main__':

    matches = open('../matches_line_breaks/matches_Spain.json','r', encoding='utf-8')
    cl=matches.readline()

    targetId='676'

    while(cl):
        curr_line=json.loads(cl)

        if targetId in curr_line['teamsData'].keys():
            print(curr_line['wyId'])

        cl=matches.readline()
    