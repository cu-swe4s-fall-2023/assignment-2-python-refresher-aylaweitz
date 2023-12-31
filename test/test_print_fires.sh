# mamba install wget
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

path='../src'
fig_path='../doc'

run basic_test python $path/print_fires.py --file_name '../test_data.csv'
assert_exit_code 0

# mean
run return_mean python $path/print_fires.py --file_name '../test_data.csv' --operation "mean"
assert_exit_code 0

# median
run return_median python $path/print_fires.py --file_name '../test_data.csv' --operation "median"
assert_exit_code 0

# standard deviation
run return_std python $path/print_fires.py --file_name '../test_data.csv' --operation "std"
assert_exit_code 0

# plotting histogram
run plotting_hist python $path/plotting.py
assert_equal $fig_path/fire_hist.jpg $( ls $fig_path/fire_hist.jpg )