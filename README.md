# Mail Sender

This is an application to send mails to a mail list. It receives a spreadsheet
with the mail addresses and a file with the content, then send the content to
every mail listed in the spreadsheet.


## Usage

```
$ mailsender <mail_config> <mail_list> <mail_content>
```

* `<mail_config>`: JSON file with the mail server parameters
* `<mail_list>`: the spreadsheet containing the addresses
* `<mail_content>`: the file with the body of the message


## Format Of The Files

### Spreadsheet

The spreadsheet must start from A1 with the following columns:

* `name`: the name of the receiver
* `email`: the e-mail address

> For the moment, the program only accept *.csv* files.


### Mail content

This must be a **plain text file** with the message to be sent. You can include
a line with the tag `Subject: ` followed by the subject of the message. This
line can go at any point in the file, but is recommended to put it near the top,
for easy access. Also, only the first occurrence of `Subject: ` will be
considered.

Some fields could be used and they will be overwritten by the program in the
outgoing message. The fields are the following:

* `__name__`: to be substituted by the name of the receiver
* `__email__`: to be substituted by the e-mail address of the receiver
* `__date__`: to be substituted by the current date

Te content of the file can be just plain text or HTML. In the last case, it must
start with the *DOCTYPE* declaration.

> The file extension is irrelevant.

#### Text Message Example

```
Subject: Test Mail in Plain Text Format.

Hi, __name__!

This is a test message send from Mail Sender.

It's always a pleasure write you at __email__ on this day __date__.

Have a nice day, __name__.

```

#### HTML Message Example

```
<!DOCTYPE html>
Subject: Test Mail in HTML.
<html>
<head>
	<meta charset="utf-8">
	<title>Test Message</title>
</head>
<body>
	<p>
		Hi, __name__:
	</p>
	<p>
		This is a test of an HTML mail from <b>Mail Sender</b>.
	</p>
</body>
</html>
```


### Configuration File

This is a JSON file that contain the mail server settings for outgoing mails.

#### Example

```
{
	"user": "user@example.com",
	"password": "Password123",
	"server": "smtp.example.com",
	"port": 587
}
```

# Contact Information

Developed by Marcelo Freri.

Contact me at contact@mfreri.com.

Follow me at https://mastodon.social/@mfreri.

