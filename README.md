[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# U.S. Fires

## Introduction
In this project, we investigate the number of forest and savanna fires in the United States.

## Results
We find a positive correlation between forest and savanna fires in the U.S, and that there were consistently more forest fires than savanna fires in the years 1990-2000. We also find that the mean number of forest fires that occur in a year in the U.S. is approximately 1929 fires while the mean number of savanna fires is 1393. While there are some years where there were significantly more forest fires than average, the number of forest and savanna fires in a year hasn't dramatically increased in the U.S. from 1990 to 2020.

##Methods
To obtain these results, we plotted the number of number of forest fires vs. the number of savanna fires in a year (see fire_hist.jpg). We also plotted the number of forest fires as a function of the number of savanna fires (see fores_v_savanna.jpg). We plotted the number of forest and savanna fires as a function of year (see forest_v_year.jpg).


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
