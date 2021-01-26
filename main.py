import gspread
from twitter import *

consumer_key = 'NMm9k2N2FJbjsQhDQrqqV6SUD'
consumer_secret = 'J39VyrlyyNEmwudcyKPqZ2DJ0rAj2BVD2XMSwQrpXGcsISutfV'
token = '1353867767531843584-PEnWSZU0v8skCXGjr1LFIoWaLXXVMW'
token_secret = 'hbnH3DFexdpdob2cQKdB6OF7XDKtOPEeVeugMxM73cs6k'

gc = gspread.service_account('credentials.json')
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Open a sheet from a spreadsheet in one go
wks = gc.open("john-mcclane-bot").sheet1

# Update a range of cells using the top left corner address
next_tweet = wks.acell('A2').value

# Post tweet though twitter API
t.statuses.update(
    status=next_tweet)

# Delete row on success
wks.delete_rows(2)