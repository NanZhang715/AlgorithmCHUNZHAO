#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/2/28 6:09 PM
@author: nzhang
"""
from collections import defaultdict


class Trie(object):

    def __init__(self):
        self.root = {}
        self.end_of_words = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            # node = node.setdefault(char, {})
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_of_words] = self.end_of_words

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_words in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    word, prefix = "apple", "app"
    obj = Trie()
    obj.insert(word)
    obj.insert("apana")
    print(obj.search(word))
    print(obj.startsWith(prefix))
