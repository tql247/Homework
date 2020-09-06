STOPWORDS = open('stopwords.txt', mode='r', encoding='utf-8').read().split("\n")
NON_VIETNAMESE = "[^aáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêế\
	                ềểễệfghiíìỉĩịjklmnoóòỏõọôốồổỗộơớ\
	                ờởỡợpqrstuúùủũụưứừửữựvwxyýỳỷỹỵzA\
	                ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬBCDĐEÉÈẺẼẸÊẾỀỂỄ\
	                ỆFGHIÍÌỈĨỊJKLMNOÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠ\
	                ỢPQRSTUÚÙỦŨỤƯỨỪỬỮỰVWXYÝỲỶỸỴZ ]"