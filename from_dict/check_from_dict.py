#!/usr/bin/python
# coding: utf-8

import re
import urllib
import os
import time

domain_suffix = '.com'

words_file = 'words.txt'
last_check_word_f = 'last_check_word.pkl'
api = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s"  # api地址


def get_words_from_file(words_file=words_file, init_word_line=0):
    with open(words_file) as f:
        all_words = f.readlines()

    if not init_word_line:
        if os.path.isfile(last_check_word_f):
            with open(last_check_word_f) as f:
                init_word = f.read().strip()
                print('####### last check word: %s ########' % init_word)
                try:
                    init_word_line = all_words.index(init_word+'\n')
                    print('####### index: %s' % init_word_line)
                except ValueError:
                    init_word_line = 0

    return all_words[int(init_word_line):]


def is_ava(domain):
    """判断该域名是否被注册"""
    data = urllib.urlopen(api % domain).read()
    ava_pattern = re.compile(r'<original>(.*) : .*</original>')
    result = ava_pattern.findall(data)
    if '210' in result:
        print('%s ---------> Ok' % domain)
        return True
    elif '211' in result:
        print('%s ---------> No' % domain)
        return False
    else:
        print('%s ---------> Forbidden' % domain)
        return False


def parse_word(word):
    word = word.strip()
    with open(last_check_word_f, 'w') as f:
        f.write(word)

    word = word.replace(' ', '')
    return word


if __name__ == '__main__':
    result_file = open('name.txt', 'a')
    for word in get_words_from_file():
        domain_name = parse_word(word) + domain_suffix
        if is_ava(domain_name):
            result_file.write(domain_name + '\n')
            result_file.flush()
        time.sleep(1)
    result_file.close()

