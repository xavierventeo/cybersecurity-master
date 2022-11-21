#Check TXT register (SPF) for a domain
dig holaluz.com TXT 

#Check if a domain has a DMARC setup
dig _dmarc.holaluz.com TXT

#In order to execute, remember:
#chmod +x dmarc.sh
# ./dmarc.sh   
