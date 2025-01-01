import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = '# Replace with your email'
EMAIL_PASSWORD = '# Replace with your password' 

# File paths
CSV_FILE = 'mnt/data/sheet.csv'  # Replace with your actual file path
PDF_FOLDER = 'mnt/data/pdf_folder/'

# Load data from CSV
try:
    data = pd.read_csv(CSV_FILE)
except Exception as e:
    print(f"Failed to load CSV file: {e}")
    exit(1)

def send_certificate(email, full_name, pdf_file):
    """Send a certificate to the given email."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Subject: Your Certificate of Completion'

        # Use the provided HTML file as email content
        with open("mnt/data/index.html", "r", encoding="utf-8") as html_file:
            body = html_file.read()

        # Replace placeholder with actual name
        body = body.replace("{{name}}", full_name)

        msg.attach(MIMEText(body, 'html'))

        # Attach the PDF
        attachment_path = os.path.join(PDF_FOLDER, pdf_file)
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={pdf_file}')
            msg.attach(part)

        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {email} successfully.")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")

# Process each row in the CSV
for index, row in data.iterrows():
    email = row['email']
    full_name = row['full name']
    pdf_file = row['full name'].strip() + ".pdf"

    # Send the email with the attached certificate
    send_certificate(email, full_name, pdf_file)
