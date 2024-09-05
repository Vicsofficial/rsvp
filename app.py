from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        attendance = request.form.get('attendance')
        guests = request.form.get('guests')
        guest_count = request.form.get('guest_count')

        if attendance == 'dinner':
            if guests == 'yes':
                return redirect(url_for('confirmation', guest_count=guest_count))
            else:
                return redirect(url_for('confirmation'))
        else:
            return redirect(url_for('confirmation'))

    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    guest_count = request.args.get('guest_count', 0)
    return render_template('confirmation.html', guest_count=guest_count)

if __name__ == '__main__':
    app.run(debug=True)
