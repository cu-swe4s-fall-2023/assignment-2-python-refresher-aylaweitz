set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

python print_fires.py --file_name '../Agrofood_co2_emission.csv' # works

# python print_fires.py --file_name '../Agrofood_co2_emissin.csv' # doesn't work -- filename typo
# python print_fires.py --file_name '../Agrofood_co2_emission.csv' --fires_column 0 # doesn't work -- fires_column values cannot be converted to integers

python print_fires.py --file_name '../Agrofood_co2_emission.csv' --operation "mean"
python print_fires.py --file_name '../Agrofood_co2_emission.csv' --operation "median"
python print_fires.py --file_name '../Agrofood_co2_emission.csv' --operation "std"