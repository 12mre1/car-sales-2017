import pandas as pd
import plotly.graph_objs as go
import numpy as np

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
data = pd.read_csv('data/Car_sales.csv')
cols_to_keep = ['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']

def clean_data(df, cols_to_keep = cols_to_keep):
    # Keep columns of interest
    df = df[cols_to_keep]
    # Adjust col names
    df.columns = ['manu', 'model', 'sales', 'price', 'hp', 'fuel']
    # Drop short thousand notation
    df['sales'] = df['sales']*1000
    df['price'] = df['price']*1000
    
    return df


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    df = clean_data(df = data)

    ### Graph One: Sales Revenue by Manufacturer (top 5 bar)
    
    # Extract manufacturers
    manufacturers = df['manu'].unique().tolist()
    # Create revenue in Millions
    df['revenue'] = df['sales']*df['price'] #// (10*9)
    # Group by revenue and sum across manufacturer
    rev_by_manu = df.groupby(['manu'])['revenue'].sum().reset_index()
    # Sort manus by rev and take top 5
    sorted_rev = rev_by_manu.sort_values('revenue', ascending=False).iloc[:5,:] 

    top_5_manu = [name for name in sorted_rev['manu'].tolist()]
    top_5_rev = [round(num, 3) for num in sorted_rev['revenue'].tolist()]
    
    graph_one = []    
    graph_one.append(
      go.Bar(
      x = top_5_manu,
      y = top_5_rev,
#       marker_color = 'red',    
      )
    )

    layout_one = dict(title = 'Top 5 Auto Manufacturers By Revenue ($B)',
                xaxis = dict(title = 'Manufacturer'),
                yaxis = dict(title = '2017 Revenue ($Billions)'),
                )

    ### Graph two: Fuel Capacity clustered by manufacturer
    
    
    graph_two = []
    graph_two.append(
        go.Scatter(
            x = df['model'].tolist(),
            y = df['fuel'].tolist(),
            mode='markers',
            marker=dict(
            color = 'red'
            ),
        )
    )

    layout_two = dict(title = 'Fuel Capacity By Manufacturer and Model',
                xaxis = dict(title = 'Model',),
                yaxis = dict(title = 'Fuel Capacity (Miles/Gal)'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    # Gather Make and model into one var
    df['car'] = df['manu'] + ' ' + df['model']
    # Sort by price and extract top 10
    top_10_price = df.sort_values('price', ascending=False).iloc[:10,:]

    # Remove manu and model cols
    table_data = top_10_price[['car', 'price', 'sales', 'hp', 'fuel']]
    table_data['sales'] = table_data['sales'].astype(int)
    
    # Get cars and prices for graph
    top_10_price_cars = table_data['car'].tolist()
    top_10_price_prices = table_data['price'].tolist()
    
    # Build the third graph
    graph_three = []
    graph_three.append(
      go.Bar(
      x = top_10_price_cars,
      y = top_10_price_prices,
      )
    )

    layout_three = dict(title = '10 Most Expensive Cars',
                xaxis = dict(title = ''),
                yaxis = dict(title = 'Price')
                       )
    
    # Chart 4 is a Horsepower by manufacturer
    hp_by_manu = df.groupby(['manu'])['hp'].mean().reset_index()
    # Sort manus by rev and take top 5
    sorted_hp = hp_by_manu.sort_values('hp', ascending=False)
    # Convert to nested list for placement in dashboard
    manufacturers = [name for name in sorted_hp['manu'].tolist()]
    sorted_hp_values = [num for num in sorted_hp['hp'].tolist()]
    graph_four = []
    graph_four.append(
      go.Scatter(
        x = manufacturers,
        y = sorted_hp_values,
        mode = 'markers',
        marker=dict(
            color = 'red'
        ),
       )
     )

    layout_four = dict(title = 'Average Horsepower by Manufacturer',
                xaxis = dict(title = 'Manufacturer'),
                yaxis = dict(title = 'Mean Horsepower'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures