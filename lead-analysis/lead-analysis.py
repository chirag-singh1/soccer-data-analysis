import argparse
import halftime

if __name__ == '__main__':

    #Setup argument parsing
    parser=argparse.ArgumentParser(description='Generate a variety of graphics centered around the halftime lead of specific games')
    parser.add_argument('-A','--percentage_adjust',required=False,nargs=1, default='False', choices=['True','False'])
    parser.add_argument('-C','--competitions',required=False,nargs='*',default='all',
    choices=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship'])
    args = parser.parse_args()

    #Choose competitions based on arguments
    if args.competitions == 'all':
        competitions=['Spain', 'England', 'France','Germany','Italy','World_Cup','European_Championship']
    else:
        competitions=args.competitions
    
    halftime.run_analysis(competitions,args.percentage_adjust[0])