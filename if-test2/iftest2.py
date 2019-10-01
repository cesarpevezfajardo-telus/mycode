#!/usr/bin/env python3

ipchk = input('Apply an IP address: ') #prompts the user for input

if ipchk == '192.168.0.1': # If the Ip matches this one
    print('it seems like the IP: ' + ipchk + ' is not valid')
elif ipchk: # If any data is provided, then it is true
    print('Looks like the IP was set: ' + ipchk ) # Indented under 'if'
else: # If no data is provided, then show error
    print('You did not provide any data')

