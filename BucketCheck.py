import urllib
import sys
bucket = sys.argv[1]
domain = "http://"+bucket+".s3.amazonaws.com"
response = urllib.urlopen(domain)
hallo = response.read()
if "NoSuchBucket" in hallo:
    print "No such Bucket."
if "AccessDenied" in hallo:
    print "Bucket is real"
