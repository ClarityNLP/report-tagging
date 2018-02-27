import util
import re
import configparser
import psycopg2
import psycopg2.extras
import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
from collections import Counter

def test(t):
    # DB connection
    print t
    conn = psycopg2.connect(util.conn_string)
    cursor = conn.cursor()

    #cursor.execute("""SELECT tag_name FROM nlp.unigram_tag_map where unigram in %s """, (t, ))
    #cursor.execute("""SELECT tag_name FROM nlp.unigram_tag_map where strpos(%s, unigram) > 0 """, (t, ))
    cursor.execute("""SELECT tag_name from nlp.bigram_tag_map where strpos(%s, bigram) = 1 ORDER BY tag_name DESC LIMIT 1 """, (t,))
    result = cursor.fetchall()
    return result
    conn.close()


def generateTags(reportName):
    # DB connection
    conn = psycopg2.connect(util.conn_string)
    cursor = conn.cursor()


    # Resultant list
    tags = []

    # Curating input
    reportName = reportName.strip()
    searchString = reportName.split()

    # Generating bigrams
    token = RegexpTokenizer(r'\w+')
    token = token.tokenize(reportName.lower())
    bigrams = ngrams(token, 2)

    completedWords = []

    for i in bigrams:
        gram = ' '.join(i)
        #gram = '%' + gram + '%'

        try:
            #cursor.execute("""SELECT tag_name FROM nlp.bigram_tag_map where bigram LIKE %s OR strpos(%s, bigram) > 0 ORDER  BY tag_name DESC LIMIT 1 """, (gram,gram))
            #cursor.execute("""SELECT tag_name FROM nlp.bigram_tag_map where bigram LIKE %s OR strpos(%s, bigram) > 0 ORDER  BY tag_name DESC LIMIT 1 """, (gram,gram))
            cursor.execute("""SELECT tag_name FROM nlp.bigram_tag_map where strpos(%s, bigram) = 1 ORDER  BY tag_name DESC LIMIT 1 """, (gram,))
            result = cursor.fetchall()

            if len(result)>0:
                completedWords.append(i[0])
                completedWords.append(i[1])

            for j in result:
                tags.append(j[0])

            # cursor.execute("""SELECT tag_name FROM nlp.bigram_tag_map where strpos(%s, bigram) > 0 ORDER  BY tag_name DESC LIMIT 1 """, (gram,))
            # result = cursor.fetchall()
            #
            # if len(result)>0:
            #     completedWords.append(i[0])
            #     completedWords.append(i[1])
            #
            # for j in result:
            #     tags.append(j[0])


        except Exception as ex:
            print "Failed to extract data from the DB-bigrams"
            print str(ex)

    # Removing visited terms
    for i in completedWords:
        if i in token:
            token.remove(i)

    # Generating unigrams
    unigrams = ngrams(token, 1)

    for i in unigrams:
        gram = str(i[0])
        #gram = '%' + gram + '%'
        try:
            #cursor.execute("""SELECT tag_name FROM nlp.unigram_tag_map where unigram LIKE %s OR strpos(%s, unigram) > 0 ORDER  BY tag_name DESC LIMIT 1 """, (gram,gram))
            #cursor.execute("""SELECT tag_name FROM nlp.unigram_tag_map where unigram LIKE %s OR strpos(%s, unigram) = 1 ORDER  BY tag_name DESC LIMIT 1 """, (gram,gram))
            cursor.execute("""SELECT tag_name FROM nlp.unigram_tag_map where strpos(%s, unigram) = 1 ORDER  BY tag_name DESC LIMIT 1 """, (gram,))
            result = cursor.fetchall()

            for j in result:
                tags.append(j[0])

            # cursor.execute("""SELECT tag_name FROM nlp.unigram_tag_map where strpos(%s, unigram) > 0 ORDER  BY tag_name DESC LIMIT 1 """, (gram,))
            # result = cursor.fetchall()
            #
            # for j in result:
            #     tags.append(j[0])



        except Exception as ex:
            print "Failed to extract data from the DB-unigrams"
            print str(ex)

    conn.close()
    return tags
