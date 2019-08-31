#!/bin/python3

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def month_to_str(m):
    return{
            1 : 'Jan',
            2 : 'Feb',
            3 : 'Mar',
            4 : 'Apr',
            5 : 'May',
            6 : 'Jun',
            7 : 'Jul',
            8 : 'Aug',
            9 : 'Sep', 
            10 : 'Oct',
            11 : 'Nov',
            12 : 'Dec'
    }[m].upper()

def get_time():
    d = datetime.now()
    year = d.year
    month = d.month
    day = d.day
    return year, month_to_str(month), day

@app.route('/', methods=['GET', 'POST'])
def form():

    config=dict()

    if request.method == 'POST':
        keys=['group_authority', 'kjn', 'dojang',
            'head_instructor', 'admin2', 'admin3',
            'date_year', 'date_month','date_day']
        for k in keys:
            config[k] = request.form.get(k)
    else:
        config['date_year'], config['date_month'], config['date_day'] = get_time()
        config['group_authority'] = 'WOODBRIDGE TAEKWON-DO GROUP - GRAND MASTER J. CARIATI IX DAN'
        config['kjn'] = 'GRAND MASTER J. CARIATI IX DAN'
        config['dojang'] =  'Woodbridge Taekwondo'
        
    return render_template('form.html', **config)
