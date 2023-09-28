from my_utils import get_column
import argparse

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

args = parser.parse_args()

fires = get_column(args.file_name, args.country_column, args.country, args.fires_column)
print(fires)
