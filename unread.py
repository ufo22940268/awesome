#/usr/bin/env python
#import httplib
#import urllib
##conn = httplib.HTTPSConnection("https://ccheng@grandstream.com:aa890525@mail.google.com/mail/feed/atom")
#print urllib.quote("https://ccheng@grandstream.com:aa890525@mail.google.com/mail/feed/atom", "")
#conn = httplib.HTTPSConnection("https://" + urllib.quote("ccheng@grandstream.com:aa890525@mail.google.com/mail/feed/atom", ""))
#conn.request("GET", "")
#data = conn.getresponse().read()
#print(data)
import urllib2
import base64

u = "ccheng@grandstream.com"
p = "aa890525"

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_encoded = base64.encodestring('%s:%s' % (u, p))[:-1]
req = urllib2.Request('https://mail.google.com/mail/feed/atom')
req.add_header('Authorization', 'Basic %s' % auth_encoded)
response = urllib2.urlopen(req)
