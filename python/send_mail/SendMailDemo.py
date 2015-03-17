from SendMail import Mail

if __name__ == '__main__':
	# SMTP settings
	host = "your_host"
	port = 25
	username = "your_username"
	password = "your_passport"
	email = "your_email"

	# Create a Mail object
	mailDemo = Mail(host, port, username, password, email)
	# Login
	mailDemo.login()

	# Mail settings
	mailTo = ["sendto_email"]
	senderName = "sender_name_displayed"
	subject = "mail_subject"
	content = "mail_content"

	# Send a text mail
	mailDemo.sendTextMail(senderName, mailTo, subject, content)