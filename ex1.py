# -*- encoding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import re

# Page 5: Web Crawler from qiushibaike
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()

# Page 6:
def demo_string():
    print "I love Ctrip!"
    print 'I love Ctrip!'
    print "I love 'Ctrip'!"
    print 'I love "Ctrip"!'
    print "I love \'Ctrip\'!"
    print "I" + " love" + " Ctrip" + "!"
    # string function: capitaliza(), replace(), startwith(), endwith()
    # len(), split(), find(), lstrip(), rstrip(), join()
    stra="hello, world!"
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')
    print stra.startswith('hello')
    print stra.endswith('d')
    print len(stra)
    print stra.split(' ')
    print stra.find('!')
    strb="\n\rhello nowcoder\r\n"
    print strb.lstrip()
    print strb.rstrip()
    print '-'.join(['a', 'b', 'c'])
    # make string turn into digit: ``;str;repr
    temp=42
    print "The temperature is " + `temp`
    # long string
    print '''This is a very long string.
Still continue...
Still here.'''
    # newline
    print 1+2\
    +3
    # original string
    print r'Let\'s go!\\'


def demo_operator():
    pass

def demo_buildinfunction():
    pass

def demo_controlflow():
    pass

def demo_list():
    pass

def demo_tuple():
    pass

def demo_dict():
    pass

def demo_set():
    pass

def demo_exception():
    pass

def demo_random():
    pass

def demo_re():
    pass

if __name__ == '__main__':
    # comments
    # print "Hello, nowcoder!"
    # qiushibaike()
    demo_string()

