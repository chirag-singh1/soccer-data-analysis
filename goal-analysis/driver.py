import argparse
import get_goals

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Generate a variety of datasets centering around goals and their buildup')
    parser.add_argument('-P','--player',required=False,nargs='*',default=['0'])
    parser.add_argument('-C','--competitions',required=False,nargs='*',default=['all'],
    choices=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship'])
    parser.add_argument('-M','--match',required=False,nargs='*',default=['0'])
    parser.add_argument('-T','--team', required=False, nargs='*',default=['0'])
    parser.add_argument('-G','--goal',required=False,nargs='*',default=['0'])
    parser.add_argument('-B','--show_buildup',required=False,nargs='*',default=['False'], choices=['True','False'])
    args=parser.parse_args()

    get_goals.run_analysis(args.competitions[0],int(args.match[0]),int(args.team[0]),int(args.player[0]),int(args.goal[0]),args.show_buildup[0])