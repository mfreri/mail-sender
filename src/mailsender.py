#!/usr/bin/python3
#encoding: utf-8


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datafiles import read_csv
from datafiles import read_json
from datafiles import read_txt
from datetime import datetime
import smtplib
import ssl
import sys


_VERSION = "1.1"
_DATE = "2023-05-05"
_CONTACT = "info@mfreri.com"
_HELP = f"""\
Send mails to a list of recipients.

USAGE:
    mailsender [options] <mail_config_file> <mail_list_file> <mail_content_file>

ARGUMENTS:
    <mail_config_file>        JSON file with mail server settings.
    <mail_list_file>          CSV file with the list of receivers.
    <mail_content_file>       TXT or HTML file with the content of the messages.

OPTIONS:
    -h, --help                Show this help.
    -v, --version             Display version info.

COPYRIGHT:
    MailSender (C) 2023 Marcelo Freri.
    This program comes with ABSOLUTELY NO WARRANTY.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License (GPL-3) as published
    by the Free Software Foundation.

SOURCE CODE:
    https://github.com/mfreri/mailsender

CONTACT:
    Developed by Marcelo Freri <{_CONTACT}>.
"""


def main():
	# Parameters management
	# mailsender <mail_config_file> <mail_list_file> <mail_content_file>
	if "--version" in sys.argv or "-v" in sys.argv:
		# Display program version
		print(f"MailSender version {_VERSION} from {_DATE}.")
		exit(0)
	elif "--help" in sys.argv or "-h" in sys.argv:
		# Show help
		print(_HELP)
		exit(0)
	if len(sys.argv) == 4:
		# Takes the names of the files from the command line
		mail_config_file  = sys.argv[1]
		mail_list_file    = sys.argv[2]
		mail_content_file = sys.argv[3]
	else:
		print("Syntax error. Use '--help' for more information.")
		exit(1)

	# Reads the configuration file
	mail_config    = read_json(mail_config_file)
	# Breaks down mail server settings
	mail_sender    = mail_config["user"]
	mail_smtp      = mail_config["server"]
	mail_port      = mail_config["port"]
	mail_password  = mail_config["password"]
	
	# Reads the mail list from the file
	mail_receivers = read_csv(mail_list_file)
	
	# Reads the message content from the file
	mail_body      = read_txt(mail_content_file)
	
	# Sends the messages
	print("Sending mails...")
	mail_counter = 0
	for mail_receiver in mail_receivers:
		# Prepares the message
		keywords_list = [
			("__name__", mail_receiver["name"]),
			("__email__", mail_receiver["email"]),
			("__date__", str(datetime.now())[:10]),
		]
		mail_body_edited = replace_keywords(mail_body, keywords_list)
		# Sends the message
		send_mail(
			mail_sender,
			mail_smtp,
			mail_port,
			mail_password,
			mail_receiver["email"],
			mail_body_edited
		)
		mail_counter += 1
	print(mail_counter, "mail(s) sended.")


# Replaces the keywords from a given text
def replace_keywords(text, keywords):
	output = text
	for k in keywords:
		output = output.replace(k[0], k[1])
	return output


# Gets the content of a field from a text
def get_field_from_text(text, fieldname):
	output = [text, ""]
	lines = text.splitlines()
	for line in lines:
		if line.startswith(fieldname):
			output[0] = text.replace(line, "")
			output[1] = line.replace(fieldname, "").strip()
			break
	return output


# Sends an email to a recipient
def send_mail(sender, smtp_server, smtp_port, password, receiver, message):
	msg = MIMEMultipart('alternative')
	msg['From'] = sender
	msg['To'] = receiver
	content, subject = get_field_from_text(message, "Subject:")
	msg['Subject'] = subject
	# Detects if the content is in HTML or Text format
	if message.startswith("<!DOCTYPE html>"):
		msg.attach(MIMEText(content, 'html'))
	else:
		msg.attach(MIMEText(content, 'plain'))
	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, smtp_port) as server:
		server.ehlo()
		server.starttls(context=context)
		server.login(sender, password)
		server.send_message(msg=msg)

# Fake send mail function for testing purposes
def send_mail_fake(sender, smtp_server, smtp_port, password, receiver, message):
	print("* Fake sending.")
	print(message)


if __name__ == '__main__':
	main()
