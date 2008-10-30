#! /usr/bin/env python

import twitter
from ConfigParser import ConfigParser
from optparse import OptionParser
from sys import argv

def parseOptions(argv) :
    parser = OptionParser()

    parser.add_option('-u', '--update',
                      action = 'store_const',
                      const  = 'update',
                      dest   = 'action')

    parser.add_option('-t', '--test',
                      action = 'store_const',
                      const  = 'test',
                      dest   = 'action')

    options, args = parser.parse_args(argv[1:])

    return options, args

def initAPI() :
    parser = ConfigParser()
    parser.read('.chirprc')

    api = twitter.Api(parser.get('authentication', 'username'),
                      parser.get('authentication', 'password'))

    return api

def main() :
    options, args = parseOptions(argv)

    api = initAPI()

    if options.action == 'update' :
        status = []
        while True :
            try :
                status.append(raw_input())
            except EOFError :
                break

        status = '\n'.join(status)

        if len(status) > 140 :
            print "Message is too long, must be less than 140 characters."
            print "Current message is %d characters long." % len(status)
        else :
            api.PostUpdate(status)
            print "Posted update."

    elif options.action == 'test' :
        print args

    return

if __name__ == '__main__' :
    main()

