import socket
import urllib
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bucket = raw_input("Bucketname: ")
domain = "http://"+bucket+".s3.amazonaws.com"
response = urllib.urlopen(domain)
hallo = response.read()
if "NoSuchBucket" in hallo:
    print "No such Bucket."
if "AccessDenied" in hallo:
    print "Bucket is real"
s.close()