import argparse
import halftime
import nextgoal
import shot_frequency

if __name__ == '__main__':

    #Setup argument parsing
    parser=argparse.ArgumentParser(description='Generate a variety of graphics centered around the halftime lead of specific games')
    parser.add_argument('-A','--analysis',required=False,nargs=1, default='halftime-lead', choices=['halftime-lead','halftime-percent-adjusted','next-goal','next-goal-adjusted', 'shot-frequency'])
    parser.add_argument('-C','--competitions',required=False,nargs='*',default='all',
    choices=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship'])
    args = parser.parse_args()

    #Choose competitions based on arguments
    if args.competitions == 'all':
        competitions=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship']
    else:
        competitions=args.competitions
    
    #Run corresponding analysis
    if args.analysis[0] == 'halftime-lead':
        halftime.run_analysis(competitions,False)
    elif args.analysis[0] == 'halftime-percent-adjusted':
        halftime.run_analysis(competitions,True)
    elif args.analysis[0] == 'next-goal':
        nextgoal.run_analysis(competitions, False)
    elif args.analysis[0] == 'next-goal-adjusted':
        nextgoal.run_analysis(competitions, True)
    elif args.analysis[0] == 'shot-frequency':
        shot_frequency.run_analysis(competitions)

        