import my_utils
import argparse
import sys

parser = argparse.ArgumentParser(description='Pass in parameters for fire search.')

parser.add_argument('--country', 
                    type=str, 
                    default='United States of America', # default to searching for fires in US
                    help='Name of the country of interest.', 
                    required=False)

parser.add_argument('--country_column', 
                    type=int, 
                    default=0, 
                    help='Index of country column in file.', 
                    required=False)

parser.add_argument('--fires_column', 
                    type=int, 
                    default=3, 
                    help='Index of fires column in file.', 
                    required=False)

parser.add_argument('--file_name', # 'Agrofood_co2_emission.csv'
                    type=str, 
                    help='Name of the file to analyze.', 
                    required=True)

parser.add_argument('--operation',
                    type=str, 
                    default=None,
                    help='Operation to implement (mean/median/standard deviation)', 
                    required=False)

args = parser.parse_args()

def main():
    fires = my_utils.get_column(args.file_name, args.country_column, args.country, args.fires_column)

    if args.operation: # if an operation is given
        if args.operation == 'mean':
            print(f'Mean: {my_utils.calc_mean(fires)}')
        elif args.operation == 'median':
            print(f'Median: {my_utils.calc_median(fires)}')
        elif args.operation == 'standard deviation' or args.operation == 'std':
            print(f'Std: {my_utils.calc_std(fires)}')

        else:
            print(f'"{args.operation}" is an unrecognized operation name. Try something else.')
            sys.exit(5)

    else:
        print(fires)

if __name__ == '__main__':
    main()
