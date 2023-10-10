[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# U.S. Fires
This project prints the number of fires in the United States of America as a list of integers, and it prints the mean, median, and standard deviation.

## Usage
First clone this repo

```
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-aylaweitz.git
```

Then run the program using the following line:

```
bash run.sh
```

For a more generalized way of running this program, run

```
python print_fires.py --file_name <FILENAME> --country <COUNTRY> --country_column <COUNTRY COLUMN> --fires_column <FIRES_COLUMN> --operation <OPERATION>
```

where `OPERATION` can take values "mean", "median", or "std"/"standard deviation" and it will perform that operation. If no value is given for `OPERATION`, the call will return the list of integers with no operation preformed.

In our case, we are interested in the number of fires in the U.S. so `COUNTRY` = "United States of America", `COUNTRY_COLUMN` = 0, and `FIRES_COLUMN` = 3. These values are the default.

*Note*: unit and functional tests and style checks are run before any branch is pushed or any pull request is made on the main branch.
