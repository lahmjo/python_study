#------------------------------------------------------------------------------
# import libs
#------------------------------------------------------------------------------
import urllib2;
import re;

res = urllib2.urlopen("http://www.cnblogs.com/franjia/p/4384362.html");
ret = res.read();
print ret;
