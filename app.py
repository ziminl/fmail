


from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    recipient_email = request.form['recipient_email']
    subject = request.form['subject']
    message = request.form['message']
    try:
        smtp_server = 'your_smtp_server'
        smtp_port = 587 

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()


      
        username = 'your_username'  
        password = 'your_password'  


      
        server.login(username, password)
        email_message = f'Subject: {subject}\n\n{message}'
        server.sendmail(sender_email, recipient_email, email_message)
        server.quit()
        return 'mail sent'
    except Exception as e:
        return f'An error occurred: {str(e)}'

if __name__ == '__main__':
    app.run()


