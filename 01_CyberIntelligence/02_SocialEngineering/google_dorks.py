import requests

name = "Name+Surname1+Surname2"
query_google = "https://www.google.com/search?q="

site = "site:www.linkedin.com"
in_url = "inurl:"
title = "intitle:"
in_text= "intext:"
file_type = "filetype:pdf"

user_agent={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

response_site   = requests.get(query_google + site       + name,   headers = user_agent)
response_inurl  = requests.get(query_google + in_url     + name,   headers = user_agent)
response_title  = requests.get(query_google + title      + name,   headers = user_agent)
response_intext = requests.get(query_google + in_text    + name,   headers = user_agent)
response_pdf    = requests.get(query_google + file_type  + name,   headers = user_agent)

with open("z_site.log", "w") as logs_file:
    logs_file.write(response_site.text)

with open("z_inurl.log", "w") as logs_file:
    logs_file.write(response_inurl.text)

with open("z_title.log", "w") as logs_file:
    logs_file.write(response_title.text)

with open("z_intext.log", "w") as logs_file:
    logs_file.write(response_intext.text)

with open("z_pdf.log", "w") as logs_file:
    logs_file.write(response_pdf.text)