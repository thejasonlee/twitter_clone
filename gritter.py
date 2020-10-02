from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    """A starting place."""
    return render_template('home.html')

@app.route('/route1')
def test():
    return 'Just a test'

@app.route('/route2/')
def fascinating():
    return 'Just a fascinating second route. Really is something.'

@app.route('/route3/<int:my_value>')
def passing_a_simple_value_from_a_route(my_value):
    i_am_going_to_pass_this_variable = my_value
    return render_template('showing_a_value.html', context=i_am_going_to_pass_this_variable)


if __name__ == '__main__':
    app.run(debug=True)