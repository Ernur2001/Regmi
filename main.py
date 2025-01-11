from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rob'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        services = request.form['services']
        msg = Message(
                subject='Новая заявка с формы',
                sender=os.getenv('MAIL_USERNAME'),
                recipients=['regmi.main@gmail.com'],
                body=f"Имя: {name}\nEmail: {email}\nНомер: {number}\nУслуга: {services}"
            )
        mail.send(msg)
        flash('Сообщение успешно отправлено!', 'success')
        return redirect('/')
    except Exception as e:
        flash(f'Ошибка при отправке сообщения: {str(e)}', 'danger')
    return render_template('index.html')

@app.route('/en', methods=['GET', 'POST'])
def en():
    try:
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        services = request.form['services']
        msg = Message(
                subject='Новая заявка с формы',
                sender=os.getenv('MAIL_USERNAME'),
                recipients=['regmi.main@gmail.com'],
                body=f"Имя: {name}\nEmail: {email}\nНомер: {number}\nУслуга: {services}"
            )
        mail.send(msg)
        flash('Сообщение успешно отправлено!', 'success')
        return redirect('/')
    except Exception as e:
        flash(f'Ошибка при отправке сообщения: {str(e)}', 'danger')

    return render_template('index-en.html')


if __name__ == "__main__":
    app.run(debug=True)
