from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/workout-log')
def workout_log():
    return render_template('workout-log.html')

@main.route('/new-workout')
def new_workout():
    return render_template('new-workout.html')




