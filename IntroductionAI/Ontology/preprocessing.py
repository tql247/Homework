import re
from const import STOPWORDS, NON_VIETNAMESE
from pyvi import ViTokenizer, ViPosTagger

def preprocessing(quest):
	#loại bỏ các từ không phải tiếng việt
	quest = quest.replace(u'\xa0', u' ').replace("\t", " ").lower()
	quest = re.sub(NON_VIETNAMESE, " ",quest)
	#phân mảnh từ
	quest = ViTokenizer.tokenize(quest).split(" ")
	#loại bỏ stopword
	for i in range(quest.__len__()):
		if quest[i] in STOPWORDS:
			quest[i] = ""
	#nối lại thành 1 câu
	quest = " ".join(quest)
	quest = re.sub(r'\d', ' ', quest)
	quest = re.sub(r' +', ' ', quest)
	return quest
	
A = 'trường có bao nhiêu cơ sở toàn quốc?'
print(preprocessing(A)) 
	