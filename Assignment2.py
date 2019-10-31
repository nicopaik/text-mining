from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

""" Import data set and process """
sms = pd.read_csv('SMSSpamCollection.txt', sep="\t", header = None, encoding = 'utf-8') #Import data set separated by tabs
sms.columns = ['label', 'message'] #rename column headers

""" Generate spam word cloud """
spam_words = ' '.join(list(sms[sms['label'] == 'spam']['message'])) #Select all the rows labeled spam and join inside a list to create a list of all the words
spam_word_cloud = WordCloud(width = 1280,height = 720).generate(spam_words) #Generate wordcloud

""" Visualize the spam word cloud """
plt.figure(figsize = (15, 10), facecolor = 'w') #Size and background color properties
plt.imshow(spam_word_cloud) #used to insert image to matplotlib visual
plt.axis('off') #Remove axis marks
plt.show() #Shows the wordcloud

""" Generate ham word cloud """
ham_words = ' '.join(list(sms[sms['label'] == 'ham']['message'])) #Select all the rows labeled ham and join inside a list to create a list of all the words
ham_word_cloud = WordCloud(width = 1280,height = 720).generate(ham_words) #Generate wordcloud

""" Visualize the ham word cloud """
plt.figure(figsize = (15, 10), facecolor = 'w') #Size and background color properties
plt.imshow(ham_word_cloud) #used to insert image to matplotlib visual
plt.axis('off') #Remove axis marks
plt.show() #Shows the wordcloud