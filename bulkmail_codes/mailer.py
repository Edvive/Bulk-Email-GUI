import os

from .mailfunctions import sendnovar, sendvar
from json import load, loads


class TextMail:
    def __init__(
        self, filename, type, template=False, email_field="email", subject="subject"
    ):
        self.database = filename
        self.variables = dict()
        self.email_field = email_field
        self.subject = subject
        if type not in ["plain", "html"]:
            raise ValueError("Type must be either 'plain' or 'html'")
        else:
            self.type = type
        # self.constants (to be)

        # Loading template
        if template:
            self.template = open(template, "r").read()

    def add_variables(self, variables: dict):
        self.variables.update(variables)

    # def add_constants(self, constants:dict):
    #    pass (TO BE)

    def set_template(self, filename: str):
        self.template = open(filename, "r").read()

    def set_email_field(self, fieldname: str):
        self.email_field = fieldname

    def set_subject(self, text: str):
        self.subject = text

    def send(self):
        with open('credentials.json','r', encoding='utf-8') as creds:
            cred = creds.read()
        cred = loads(cred)
        self.credentials = {
            "SMTP_HOST": cred.get("SMTP_HOST"),
            "SMTP_PORT": cred.get("SMTP_PORT"),
            "SENDER_EMAIL": cred.get("SENDER_EMAIL"),
            "SENDER_PASSWORD": cred.get("SENDER_PASSWORD"),
        }

        if not bool(self.variables):
            sendnovar(
                self.database,
                self.template,
                self.subject,
                self.email_field,
                self.credentials,
                self.type,
            )
        else:
            sendvar(
                self.database,
                self.template,
                self.subject,
                self.email_field,
                self.variables,
                self.credentials,
                self.type,
            )
