# Script to open list of standard work websites

import webbrowser

work_websites = [
    'https://mail.google.com/mail/u/0/#inbox',
    'https://calendar.google.com/calendar',
    'https://accountingprose.teamwork.com/#/home/dashboards',
    'https://accountingprose.teamwork.com/desk',
    'https://accountingprose.app.box.com/',
    'https://go.xero.com/'
]

for website in work_websites:
    webbrowser.open(website)
