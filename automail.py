import yagmail
import os
import datetime
import Info
import pandas as pd
import numpy as np


def send_mail():
    date = datetime.date.today().strftime("%B %d, %Y")
    path = 'Attendance'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

    df = pd.read_csv(r'EmployeeDetails\EmployeeDetails.csv')
    receivers = df["email"]

    newest = files[-1]
    filename = newest
    sub = "Attendance Report for " + str(date)
    body = "Attendance Submitted."

    for receiver in receivers:
        if pd.isnull(receiver):
            continue
        else:
            yag = yagmail.SMTP(Info.EMAIL_ID, Info.PASSWORD)

            yag.send(
                to=receiver,
                subject=sub,
                contents=body,
                attachments=filename
            )
            print("Email Sent to " + receiver)


if __name__ == '__main__':
    send_mail()
