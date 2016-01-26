#!/usr/bin/env python3
# encoding: utf-8

import yagmail

yag = yagmail.SMTP('bzatrok@gmail.com')

sender = 'bzatrok@gmail.com'
send_to = input("Type an email address to send the output to: ")
receivers = [send_to]

with open('output.txt', 'r') as output_file:
	message = output_file.read()
	yag.send(contents = message)
