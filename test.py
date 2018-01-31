#!/usr/bin/env python3

from src.TextCorpus import TextCorpus
from src.Text import Text
from src.Network import Network
from src.rule_set import english
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
text_filename = os.path.join(
	current_dir, 'datasets/bbc-news/news/tech/ink-helps-drive-democracy-in-asia.txt'
)

print('Analyzing ' + text_filename)
corpus = TextCorpus(os.path.join(current_dir, 'datasets/bbc-news.json'))
text = Text(corpus, open(text_filename, mode='r', encoding='utf-8').read())
print('Text of ' + str(len(text.terms)) + ' terms with average score of ' + str(text.avg_score))

net = Network(english)
net.merge(text)
print('To be continued...')

terms, ctx = english.apply(
	[('ink', 'NN'), ('helps', 'VBZ'), ('drive', 'JJ'), ('democracy', 'NN')],
	0
)
print(terms, ctx)
