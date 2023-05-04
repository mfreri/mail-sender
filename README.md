# Mail Sender

This is an application to send mails to a mail list. It recieve a spreadsheet
with the mail adresses and a file with the content, then send the content to
every mail listed on the spreadsheet.


## Usage

```
$ mailsender <mail_config> <mail_list> <mail_content>
```

* `<mail_config>`: JSON file with the mail server parameters
* `<mail_list>`: the spreadsheet contaning the addresses
* `<mail_content>`: the file with the body of the message


## Format Of The Files

### Spreadsheet

The spreadsheet must start from A1 with the following columns:

* `name`: the name of the receiver
* `email`: the e-mail address

> For the moment, the program only accept *.csv* files.


### Mail content

This must be a **plain text file** with the message to be sent. It must start
with the keyword `Subject: ` followed by the subject of the message. The body
can start on the next line.

Some fields could be used and they will be overwritten by the program in the
outgoing message. The fields are the following:

* `__name__`: to be substituted by the name of the receiver
* `__email__`: to be substituted by the e-mail address of the receiver
* `__date__`: to be substituted by the current date


### Configuration File

This file contains the mail server settings for outgoing mails. It's a *JSON*
file.

```
{
	"user": "user@example.com",
	"password": "Password123",
	"server": "smtp.example.com",
	"port": 587
}
```

# Contact Information

Developed by Marcelo Freri. Contact me at mfreri@proton.me. Follow me at https://mastodon.social/@mfreri.

