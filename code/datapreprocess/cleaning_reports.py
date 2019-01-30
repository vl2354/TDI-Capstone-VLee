# -*- coding: utf-8 -*-
#script that use certain classes to clean and filter the annual reports text files
#python 2.7

#import libraries
import codecs
BOM = codecs.BOM_UTF8.decode('utf8')
import re
import string
#import glob
import os
from os.path import basename
import io
#import numpy as np
import nltk
from nltk.corpus import stopwords
import sklearn
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from gensim.parsing.porter import PorterStemmer

#################################################################################
# improved list from Stone, Denis, Kwantes (2010)
# i removed the words toward - towards
#This list wasn't use
STOPWORDS = """
a about above across after afterwards again against all almost alone along already also although always am among amongst amoungst amount an and another any anyhow anyone anything anyway anywhere are around as at back be
became because become becomes becoming been before beforehand behind being below beside besides between beyond bill both bottom but by call can
cannot cant co computer con could couldnt cry de describe
detail did do doesn done down due during
each eg eight either eleven else elsewhere empty enough etc even ever every everyone everything everywhere except few fifteen
fify fill find fire first five for former formerly forty found four from front full further get give go
had has hasnt have he hence her here hereafter hereby herein hereupon hers herself him himself his how however hundred i ie
if in inc indeed interest into is it its itself keep last latter latterly least less ltd
just
kg km
made many may me meanwhile might mill mine more moreover most mostly move much must my myself name namely
neither never nevertheless next nine no nobody none noone nor not nothing now nowhere of off
often on once one only onto or other others otherwise our ours ourselves out over own part per
perhaps please put rather re
quite
rather really regarding
same see seem seemed seeming seems serious several she should show side since sincere six sixty so some somehow someone something sometime sometimes somewhere still such system take ten
than that the their them themselves then thence there thereafter thereby therefore therein thereupon these they thick thin third this those though three through throughout thru thus to together too top twelve twenty two un under
until up unless upon us used using
various very very via
was we well were what whatever when whence whenever where whereafter whereas whereby wherein whereupon wherever whether which while whither who whoever whole whom whose why will with within without would yet you
your yours yourself yourselves
"""


#This is the stopwords list that I finally used
STOPWORDS2 = """i  me  my  myself  we  our  ours  ourselves  you  your  yours
yourself  yourselves  he  him  his  himself  she  her  hers
herself  it  its  itself  they  them  their  theirs  themselves
what  which  who  whom  this  that  these  those  am  is  are
was  were  be  been  being  have  has  had  having  do  does
did  doing  a  an  the  and  but  if  or  because  as  until
while  of  at  by  for  with  about  against  between  into
through  during  before  after  above  below  to  from  up  down
in  out  on  off  over  under  again  further  then  once  here
there  when  where  why  how  all  any  both  each  few  more
most  other  some  such  no  nor  not  only  own  same  so
than  too  very  s  t  can  will  just  don  should  now
"""

#STOPWORDS = frozenset(w for w in STOPWORDS.split() if w)
STOPWORDS2 = frozenset(w for w in STOPWORDS2.split() if w)


#functions to clean and filter words, symbols, spaces, etc:

#Used
def remove_stopwords(s):
	return " ".join(w for w in s.split() if w not in STOPWORDS2)

#didn't use
def strip_punctuation(s):
	return re.sub("([%s]+)" % string.punctuation, " ", s)

#Used
def strip_punctuation2(s):
	return s.translate(string.maketrans("", ""), string.punctuation)

#Used
def to_lower(s):
	return s.lower()

#Used
def strip_tags(s):
	# assumes s is already lowercase
	return re.sub(r"<([^>]+)>", "", s)

#didn't use
def strip_short(s, minsize=2):
	return " ".join(e for e in s.split() if len(e) >= minsize)

#Used
def strip_numeric(s):
	return re.sub(r"[0-9]+", "", s)

#Used
def strip_non_alphanum(s):
	# assumes s is already lowercase
	# FIXME replace with unicode compatible regexp, without the assumption
	return re.sub(r"[^a-z0-9\ ]", " ", s)

#Used
def strip_multiple_whitespaces(s):
	return re.sub(r"(\s|\\n|\\r|\\t)+", " ", s)
	#return s

#didn't use
def split_alphanum(s):
	s = re.sub(r"([a-z]+)([0-9]+)", r"\1 \2", s)
	return re.sub(r"([0-9]+)([a-z]+)", r"\1 \2", s)

#didn't use
def stem_text(text):
	"""
	Return lowercase and (porter-)stemmed version of string `text`.
	"""
	p = PorterStemmer()
#    stemmer = nltk.stem.snowball.SnowballStemmer('english')
	return ' '.join(p.stem(word) for word in text.lower().split()) # lowercasing required by the stemmer
stem = stem_text

DEFAULT_FILTERS = [to_lower, strip_tags, strip_punctuation, strip_multiple_whitespaces,
				   strip_numeric, strip_non_alphanum,remove_stopwords]

################################################################################
#functions to apply filters functions to all documents
def preprocess_string(s, filters=DEFAULT_FILTERS):
	for f in filters:
		s = f(s)
	return s.split()


def preprocess_documents(docs):                      ###########esta se usa / Use este al final
	return map(preprocess_string, docs) 


def read_file(path):                      ###########esta se usa
	return open(path).read()


def read_files(pattern):
	return map(read_file, glob.glob(pattern))


######################################################################
####_Main_#######
# Main code to read folder with all documents ans apply above functions and write out new documents
#fnames = glob('/www.annualreports.com/HostedData/AnnualReportArchive/')

corpus = os.path.join('/home/jacqueline/Documents/Evan_SEC/www.annualreports.com/HostedData/Preprocessing_textfiles/output_letter')

filenames = sorted([os.path.join(corpus, fn) for fn in os.listdir(corpus)])

file_labels =[]
for file in range(len(filenames)):
	file_labels.append(basename(filenames[file]))

	#print file_labels
id1 = list(range(len(file_labels)))
	#print(id1)
r1 = []
dict1 = dict(zip(id1,file_labels))

#write out new documents as well as final word count (word count made after filter and strip words with functions)
with open('total_wordcount.csv','w') as w:
	for i in dict1:
		aux1=codecs.open(filenames[i],'r','utf-8-sig')
		l=aux1.read()
		l.lstrip(BOM)
		r1.append(l)
		name = "%s"%filenames[i][107:-7]
		proc_doc = preprocess_string(l)
		w.write(name + ',')				
		w.write('%s'%len(proc_doc))
		w.write('\n')


aux = [list(v) for v in preprocess_documents(r1)]

#print aux[1]



	#print r1

#	for i in filenames:
#		docs= []
#		with io.open(i,'r') as myfile:
#			data = myfile.read().replace('\n','').decode('utf-8')
#			docs.append(data)
#			with codecs.open('%s' %i,'w',encoding='utf-8') as z:
#				z.write('\n'.join(str(v) for v in preprocess_documents(docs)))



