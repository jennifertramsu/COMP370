from pathlib import Path
import pandas as pd

from bokeh.layouts import column
from bokeh.plotting import curdoc, figure, show
from bokeh.models import Dropdown, ColumnDataSource

ZIPCODE_COLUMN_NAME = 'incident zip'
MONTH_COLUMN_NAME = 'month'
AVERAGE_RESPONSE_TIME_COLUMN_NAME = 'avg response time'
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

plot_dataset_1 = ColumnDataSource(dict(month=[], avg_response_time=[]))
plot_dataset_2 = ColumnDataSource(dict(month=[], avg_response_time=[]))

df = None
zipcodes = None
total = None

def get_df_path(fname):
    return Path(__file__).parent.parent / 'data' / fname
    
def load_df():
    global df, total
    file = get_df_path('incident_avg.csv')
    df = pd.read_csv(file)

    total_df = df.groupby(MONTH_COLUMN_NAME)[AVERAGE_RESPONSE_TIME_COLUMN_NAME].agg('mean')
    
    total = {'month': [], 'avg_response_time': []}

    for month in MONTHS:
        if month not in total_df.index.values:
            total['month'].append(month)
            total['avg_response_time'].append(0)
        else:
            total['month'].append(month)
            total['avg_response_time'].append(total_df[month])
    
def load_zipcodes():
    global zipcodes

    file = get_df_path('incident_avg.csv')
    df = pd.read_csv(file)

    zipcodes = df[ZIPCODE_COLUMN_NAME].unique()
    zipcodes = [str(x) for x in zipcodes]

def grab_monthly_average(zipcode):

    month_avg = df.loc[df[ZIPCODE_COLUMN_NAME] == int(zipcode)][['month', 'avg response time']]

    # Add missing months
    for month in MONTHS:
        if month not in month_avg['month'].values:
            missing = {}
            missing['month'] = [month]
            missing['avg response time'] = [0]
            month_avg = pd.concat([month_avg, pd.DataFrame.from_dict(missing)], ignore_index=True)

    return {
        "month": month_avg['month'].values.tolist(),
        "avg_response_time": month_avg['avg response time'].values.tolist()
    }

def update_plot_1(event):
    global plot_dataset_1

    zip = event.item
    data = grab_monthly_average(zip)

    plot_dataset_1.data = data

def update_plot_2(event):
    global plot_dataset_2

    zip = event.item
    data = grab_monthly_average(zip)

    plot_dataset_2.data = data

def main():
    global df, zipcodes, plot_dataset_1, plot_dataset_2, total

    print("Running main...")
    
    # Loading data
    load_df()
    load_zipcodes()

    # Figure
    p = figure(title="Average Response Time by Zipcode", x_range = MONTHS, x_axis_label="Month", y_axis_label="Average Response Time (Hours)")
    p.line(x='month', y='avg_response_time', source=total, line_width=2, legend_label='Total', color='blue')
    p.line(x='month', y='avg_response_time', source=plot_dataset_1, line_width=2, legend_label='Zipcode 1', color='red')
    p.line(x='month', y='avg_response_time', source=plot_dataset_2, line_width=2, legend_label='Zipcode 2', color='green')
    p.xaxis.major_label_orientation = "vertical"

    # Dropdown
    dropdown_1 = Dropdown(label="Zipcode 1", menu = zipcodes)
    dropdown_2 = Dropdown(label="Zipcode 2", menu = zipcodes)

    dropdown_1.on_event('menu_item_click', update_plot_1)
    dropdown_2.on_event('menu_item_click', update_plot_2)

    curdoc().add_root(column(dropdown_1,dropdown_2, p))
    show(p)

main()