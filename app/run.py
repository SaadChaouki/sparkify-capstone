#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request
import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np
import json
import os

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))

def createPlot(plotType = 'Churn'):
    # Importing dataset
    weeklyData = pd.read_csv(dir_path + '/data/weeklyData.csv')

    # Create datarame that will be shown
    df = pd.DataFrame()
    df['x'] = weeklyData['dataWeek']

    # Selecting which graph will be shown based on the user selection.
    if plotType == 'Churn':
        df['y'] = weeklyData['totalChurn']
        data = [go.Line(x=df['x'], y=df['y'])]
    elif plotType == 'Sessions':
        df['y'] = weeklyData['uniqueSessions']
        data = [go.Bar(x=df['x'], y=df['y'])]
    elif plotType == 'Active Users':
        df['y'] = weeklyData['uniqueUsers']
        data = [go.Bar(x=df['x'], y=df['y'])]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

def createOptions(firstValue = 'Churn'):
    options = set(['Churn', 'Sessions', 'Active Users']) - set([firstValue])
    possibleOptions = [{'name':firstValue}]
    for option in options:
        possibleOptions.append({'name':option})
    return possibleOptions

@app.route('/')
def index():
    select = request.form.get('comp_select')
    plot = createPlot()
    return render_template('index.html',
        data=createOptions(),
        plot = plot)

@app.route("/" , methods=['GET', 'POST'])
def refresh():
    select = request.form.get('comp_select')
    plot = createPlot(select)
    return render_template('index.html',
        data=createOptions(firstValue = select),
        plot = plot)

if __name__=='__main__':
    app.run(debug=True)
