import json
from calendar import Calendar
from datetime import date

from flask import render_template, Blueprint, session

from server.month import Month
from server.models import Date, CycleEvent
from server.cycle_calculator import CycleCalculator

home_page = Blueprint('home_page', __name__)


@home_page.route('/', methods=['GET'])
def home():
    month = Month(
        Date, CycleEvent, CycleCalculator, Calendar, date.today()
    )
    # if 'month_inst' not in session:
    #     session['month_inst'] = month
    data = json.dumps(month.get_month_data())
    return render_template('calendar.html', data=data)
