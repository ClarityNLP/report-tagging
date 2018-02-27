"""
Functions to extract the n-gram and tag mappings from the report type mapper and populate into the DB
"""


import urllib, json
import util
import re
import configparser
import psycopg2
import psycopg2.extras

def load1Grams():
    url = util.one_gram_url
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    q = data['reportTypes']

    conn = psycopg2.connect(util.conn_string)
    cursor = conn.cursor()
    cursor.execute("""DELETE from nlp.unigram_tag_map;""")

    for i in q:
        if len(i['tags']) > 0:
            a = i['name']
            b = i['tags'][0]['documentSubjectMatterDomain']
            cursor.execute("""INSERT INTO nlp.unigram_tag_map (unigram, tag_name) VALUES (%s,%s);""", (a,b))

    conn.commit()
    conn.close()

def load2Grams():
    url = util.two_gram_url
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    q = data['reportTypes']

    conn = psycopg2.connect(util.conn_string)
    cursor = conn.cursor()
    cursor.execute("""DELETE from nlp.bigram_tag_map;""")

    for i in q:
        if len(i['tags']) > 0:
            a = i['name']
            b = i['tags'][0]['documentSubjectMatterDomain']
            cursor.execute("""INSERT INTO nlp.bigram_tag_map (bigram, tag_name) VALUES (%s,%s);""", (a,b))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    load1Grams()
    load2Grams()
