from flask import render_template
from flask import flash
from app import app
from app.forms import LoginForm
from main import monitor

@app.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Monitor starting for webhook {} to monitor {}'.format(
			form.webhookurl.data, form.handles.data))
		# start monitor here
		monitor(form.webhookurl.data, form.handles.data)
	return render_template('index.html', form=form)