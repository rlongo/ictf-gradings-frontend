#!/bin/python3

import tempfile

from flask import Flask, render_template, request, send_file
from datetime import datetime
from .processing import run_pipeline

app = Flask(__name__)


def month_to_str(m):
    return{
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }[m].upper()


def get_time():
    d = datetime.now()
    year = d.year
    month = d.month
    day = d.day
    return year, month_to_str(month), day


@app.route('/', methods=['GET', 'POST'])
def form():

    config = dict()

    if request.method == 'POST':
        keys = ['group_authority', 'kjn', 'dojang',
                'head_instructor', 'admin2', 'admin3',
                'date_year', 'date_month', 'date_day']

        try:
            for k in keys:
                config[k] = request.form.get(k)
                if len(config[k]) is 0:
                    raise Exception("Failed to specify value for: '%s'" % k)

            request_file = request.files['student_list']
            if not request_file:
                raise Exception("No file submitted containing student data")
           
            scratch_dir = tempfile.mkdtemp()
            file_contents = request_file.stream
            output = run_pipeline(scratch_dir, file_contents, config)
            return send_file(output)
        except BaseException as e:
            config['error_message'] = str(e)

    config['date_year'], config['date_month'], config['date_day'] = get_time()
    config['group_authority'] = 'WOODBRIDGE TAEKWON-DO GROUP - GRAND MASTER J. CARIATI IX DAN'
    config['kjn'] = 'GRAND MASTER J. CARIATI IX DAN'
    config['dojang'] = 'Woodbridge Taekwondo'

    return render_template('form.html', **config)
