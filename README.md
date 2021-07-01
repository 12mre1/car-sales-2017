# Car Sales 2017
An open-source data dashboard for the popular car sales dataset. Built with Flask, Pandas and Plotly.
You can find the original dataset [here](https://www.kaggle.com/gagandeep16/car-sales).

## Details 
I designed and built this dashboard as an exercise for Udacity's ML Engineering Nanodegree. You can see a 
modified version deployed on heroku [here](https://car-sales-2017.herokuapp.com/).
This code is slightly different, and is designed to be run locally. It uses python's plotly library
to create dynamic visualizations. The backend is handled by Flask, and the data is wrangled using
Pandas.

## Installation
To run this app, you can first clone this repo. Then I recommend creating a virtual environment
(there aren't too many dependencies). Here is an example:

```{console}
python -m venv carenv
source carenv/bin/activate
pip install -r requirements.txt
```

Then you can run the app locally:
```{console}
python myapp.py
```
Follow the URL your OS generates. Feel free to modify the visuals, or even change the data!
