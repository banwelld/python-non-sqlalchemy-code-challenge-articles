#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

auth1 = Author("Dave Banwell")
auth2 = Author("Kate Reynolds")
auth3 = Author("Paul Fedory")

mag1 = Magazine("Gifted", "Education")
mag2 = Magazine("Kindness", "Sociology")
mag3 = Magazine("Encode.this", "Computer Science")

art1 = Article(auth1, mag1, "Trials and Triumphs")
art2 = Article(auth1, mag3, "When is a List NOT a List?")
art3 = Article(auth2, mag2, "Teaching Kindness Through Song")
art4 = Article(auth2, mag1, "The Nexus of Neurodivergence and Giftedness")
art5 = Article(auth3, mag3, "The Emergence of Elixir")
art6 = Article(auth3, mag1, "The Fear of Being Extraordinary")
art7 = Article(auth1, mag1, "The Joys of Neurodivergence")
art8 = Article(auth1, mag1, "A round peg...")
art9 = Article(auth2, mag2, "The Foundations of Kindness Must be Laid Early")
art10 = Article(auth2, mag2, "Kindness: a daily practice")

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
