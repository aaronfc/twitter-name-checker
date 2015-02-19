#!/usr/env python
import urllib2

class TwitterNameChecker:
    def __init__(self):
        pass

    def exists(self, name):
        request = urllib2.Request("https://twitter.com/{}".format(name))
        try:
            response = urllib2.urlopen(request)
            doesExist = response.code == 200
        except urllib2.HTTPError, e:
            doesExist = e.code == 200

        return doesExist

    def isFree(self, name):
        return not self.exists(name)

