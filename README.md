Automail automates the sending of emails to a list of recipients using an HTML template. It is designed to read email addresses from an Excel file, personalize the email content with an HTML template, send the emails via an Outlook SMTP server, and sleep through each sending, to avoiding spam.

Project Structure:

- Automail/
    - src/
        - enterprises.xlsx: Excel file containing a list of email addresses under the column "Destinatarios".
    - front/
        - template.html: HTML template used for the email content.
    - automail.py: The main Python script for sending automated emails.

Features:

Reading Recipients from Excel: The script reads email addresses from an Excel file (enterprises.xlsx) under the column named "Destinatarios."

Customizable Email Content: Email content is generated using an HTML template (template.html), allowing for customization of the email body and structure.

SMTP Configuration: Configuration parameters for the Outlook SMTP server (host, port, login, senha) are provided.

Email Subject: The email subject is set to "CV - Analista de Dados" but can be easily customized in the script.

Personalized Email Sending: The script iterates through the list of recipients and sends personalized emails to each one, using the configured HTML template.

Delay Between Emails: To avoid potential issues with email providers and adhere to rate limits, the script includes a sleep(60) statement, causing a 60-second delay between sending each email.

Console Output: Provides informative console output, including confirmation messages for each email sent and the status of the SMTP connection.

Graceful Termination: The script terminates the SMTP connection after all emails are sent, ensuring proper closure.

How to use:

Clone the repository: https://github.com/kyliews/Automail

Navigate to the project directory: cd Automail/back/db.py
Update the following parameters based on your configuration:
login: Your email address.
senha: Your email password.

Modify the subject of the email in message ['Subject'].

Customize the HTML content in template.html to match the desired email structure and message.

Change the path of the Excel file to reflect the location of your repository.

df = pd.read_excel(r'your path\Automail/src/enterprises.xlsx')

Adjust the sleep duration in the loop (sleep(60)) based on the email service provider's rate limits.

Run the application: db.py

