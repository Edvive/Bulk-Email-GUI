import PySimpleGUI as sg
from bulkmail import TextMail
import os
from csv import reader
from socket import gaierror
from smtplib import SMTPAuthenticationError


sg.theme("Dark Red 1")


def allfields(dbfilename):
    with open(dbfilename, "r", encoding="utf-8") as db:
        database = reader(db)
        lst = next(database)
        return lst


def dbcheck(dbfilename):
    if dbfilename.split(".")[-1] != "csv":
        return "Not a csv file"
    with open(dbfilename, "r", encoding="utf-8") as db:
        lst = allfields(dbfilename)
        return f"Fields: {', '.join(lst)}"


layout = [
    [
        sg.Text("CSV File"),
        sg.InputText(size=(40, 1), key="dbfilename", readonly=True, enable_events=True),
        sg.FileBrowse(size=(10, 1), key="dbfile"),
    ],
    [sg.Text("No file imported", key="filestatus", auto_size_text=False)],
    [sg.Text("Subject:"), sg.InputText(key="subject")],
    [
        sg.Text("Template:"),
        sg.Radio(text="Plain", group_id="type", default=True, key="plain"),
        sg.Radio(text="HTML", group_id="type", key="html"),
    ],
    [
        sg.Multiline(
            size=(60, 15),
            autoscroll=True,
            default_text="Write your template here",
            key="template",
        )
    ],
    [
        sg.Text("Email Field:"),
        sg.InputText(default_text="", key="emailfield"),
    ],
    [
        sg.Text("Variable Name"),
        sg.InputText(size=(15, 1), key="variable"),
        sg.Text("Field Name"),
        sg.InputText(size=(15, 1), key="field"),
        sg.Button(button_text="Add"),
    ],
    [
        sg.Text("Email Address"),
        sg.InputText(key="username"),
    ],
    [
        sg.Text("Password"),
        sg.InputText(password_char="*", key="password"),
    ],
    [
        sg.Submit(button_text="Send", disabled=True),
        sg.Text("Status", key="status", auto_size_text=False),
    ],
]

variables = dict()

window = sg.Window("Edvive Bulk Emails", layout)

while True:
    event, values = window.read()
    if event == "Add":
        if values["field"] in allfields(values["dbfilename"]):
            variables[values["variable"]] = values["field"]
            window["variable"]("")
            window["field"]("")
            window["status"]("Variable added")
        else:
            window["status"]("Field does not exist")
    if event == "dbfilename":
        message = dbcheck(values["dbfilename"])
        window["filestatus"](message)
        if message.startswith("Fields"):
            window["Send"].Update(disabled=False)

    if event == "Send":
        window["status"]("Sending...")
        if values["html"]:
            type = "html"
        else:
            type = "plain"

        if values["emailfield"] in allfields(values["dbfilename"]):
            mail = TextMail(
                filename=values["dbfilename"],
                type=type,
                email_field=values["emailfield"],
                subject=values["subject"],
            )
            mail.template = values["template"]
            with open(".env", "w") as env:
                mailvars = f"""SMTP_HOST='smtp.gmail.com'
SMTP_PORT='587'
SENDER_EMAIL='{values['username']}'
SENDER_PASSWORD='{values['password']}'
"""
                env.write(mailvars)
            mail.add_variables(variables)
            try:
                mail.send()
                os.remove(".env")
                window["status"]("Sent!")
                variables = dict()
            except gaierror:
                window["status"]("Connection problem. Try again later.")

            except SMTPAuthenticationError:
                window["status"]("Credentials do not match.")
        else:
            window["status"]("Invalid Email Field")
    if event == sg.WIN_CLOSED:
        break

window.close()
