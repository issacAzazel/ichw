#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "linxiaohan"
__pkuid__  = "1800011791"
__email__  = "linxiaohan@pku.edu.cn"
"""


import sys
from urllib.request import urlopen
import collections
from collections import OrderedDict
import string
from string import punctuation  
import re
import urllib.error


def decodelines(aline):
    '把一个byte结构转化为str结构'
    return str(aline,encoding='utf-8-sig')



def replacelines(aline):
    '把字符串中的标点符号转化为等量空格'
    del_estr=string.punctuation+string.digits
    replace=' '*len(del_estr)
    tran_tab=str.maketrans(del_estr,replace)
    return(aline.translate(tran_tab))



def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    n=collections.Counter()
    for i in lines:
        str_new=decodelines(i)
        str_newer=replacelines(str_new)
        str_newer=str_newer.lower()
        list_0=str_newer.split()
        n.update(list_0)
    if topn>len(n):
        return (n.most_common(len(n)))
    else:
        return(n.most_common(topn))
    pass



def main():
    'main module'
    doc = urlopen(sys.argv[1])
    list_str_0=doc.readlines()
    if len(sys.argv)>2:
        list_final=wcount(list_str_0,int(sys.argv[2]))
    else:
        list_final=wcount(list_str_0)
    for i in list_final:
            print(i[0]+': '+str(i[1]))



if __name__ == '__main__':
    
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        request=urllib.request.Request(sys.argv[1])
        try:
            urllib.request.urlopen(request)
        except ValueError as err:
            print("error: {0}".format(err))
            print('please enter a integer for topn')
        except urllib.error.HTTPError as err:
            print("error: {0}".format(err.code))
            print("error: {0}".format(err.reason))
            print('please enter a correct url')
        except urllib.error.URLError as err:
            print("error: {0}".format(err.reason))
            print('please enter a correct url')
        else:
            try:
                main()
            except ValueError as err:
                print("error: {0}".format(err))
                print('please enter a integer for topn')
    
    
