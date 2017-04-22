

from nyt import NYT
import tfidflib
from wordcloud import WordCloud
import matplotlib.pyplot as plt


if __name__ == '__main__':
	print('hello world')
	nytapi = NYT()
	wordcloud = WordCloud()

	# use each month as a doc
	yrz = [(1853,12),(1853,11),(1853,10)]
	docs = [' '.join([doc['headline']['main'] for doc in nytapi.get_archive(*yrmo)['response']['docs']]) for yrmo in yrz]


	# get tfidf scores from each doc
	scores = tfidflib.getscores(docs)
	
	# print number of tokens used in the tfidf of each doc
	i = 1
	for doc in scores:
		fstr = []
		for w in doc.keys():
			fstr += [w,]*int(100*doc[w])
		wc = wordcloud.generate(' '.join(fstr))
		#plt.imshow(wc)
		plt.imsave(str(i)+'.png',wc)

		#print(len(doc.keys()))
		i += 1


	#print(scores)
	#print(len(scores))


