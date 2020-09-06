import re
import numpy as np
import pandas as pd
# import tkinter as tk
from pyvi import ViTokenizer, ViPosTagger
from const import STOPWORDS, NON_VIETNAMESE
from sklearn.neighbors import KNeighborsClassifier

TDTU = None

class concept():
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child = None
        self.p_relation = None
        self.c_relation = None
        self.feature = None
    
    def set_parent(self, parent, p_relation):
        self.parent = parent
        self.p_relation = p_relation
        
    def set_child(self, child, c_relation):
        self.child = child
        self.c_relation = c_relation
    
    def set_feature(self, feature):
        self.feature = feature
        
    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def get_child(self):
        return self.child 
    
    def get_feature(self):
        return self.feature


def make_ontology():
    global TDTU
    
    TDTU = concept('TDTU')
    
    intro = concept('intro')
    admiss = concept('admiss')
    study = concept('study')
    
    campus = concept('campus')
    address = concept('address')
    name = concept('name')
    history = concept('history')
    i_coop = concept('i_coop')
    c_coop = concept('c_coop')
    job = concept('job')
    reward = concept('reward')
    reput = concept('reput')
    infra = concept('infra')
    intro.set_child([campus, address, name, history, i_coop, c_coop, job, reward, reput, infra], 'member of')
    
    specialty = concept('specialty')
    faculty = concept('faculty')
    benchmarking = concept('benchmarking')
    strict = concept('strict')
    formal = concept('formal')
    preferential = concept('preferential')
    school_fee = concept('school_fee')
    time = concept('time')
    high_lv = concept('high_lv')
    associate = concept('associate')
    admiss.set_child([specialty, faculty, benchmarking, strict, formal, preferential, school_fee, time, high_lv, associate], 'member of')
    
    diff = concept('diff')
    exam = concept('exam')
    relearn = concept('relearn')
    proctor = concept('proctor')
    discipline = concept('discipline')
    subject_type = concept('subject_type')
    infra_conv = concept('infra_conv')
    library = concept('library')
    teacher = concept('teacher')
    study.set_child([diff, exam, relearn, proctor, discipline, subject_type, infra_conv, library, teacher], 'member of')
    
    TDTU.set_child([intro, admiss, study], 'member of')


def get_ls_ques(Path):
    ls_ques = list()
    
    with open(Path, encoding='utf-8') as file:
        text = file.readline()
        while text.__len__() != 0:
            if text[0] == '-':
                ls_ques.append(text.strip().strip('-').strip('?').strip('.').strip('-').strip(' '))
            text = file.readline()
    
    return ls_ques


def get_ls_ans(Path):
    ls_ques = list()
    
    with open(Path, encoding='utf-8') as file:
        text = file.readline()
        while text.__len__() != 0:
            if text[0] == '+':
                ls_ques.append(text.strip().strip('-').strip('?').strip('.').strip('+'))
            text = file.readline()
    
    return ls_ques


def preprocessing(quest):
    quest = quest.replace(u'\xa0', u' ').replace("\t", " ").lower()
    quest = re.sub(NON_VIETNAMESE, " ",quest)
    quest = ViTokenizer.tokenize(quest).split(" ")
    for i in range(quest.__len__()):
        if quest[i] in STOPWORDS:
            quest[i] = ""
    quest = " ".join(quest)
    quest = re.sub(r'\d', ' ', quest)
    quest = re.sub(r' +', ' ', quest)
    return quest


def extract_feature(Path):
    ls_ques = get_ls_ques(Path)
    
    feature = list()
    freq = list()
    
    for ques in ls_ques:
        ques = preprocessing(ques).strip()
        ls_word = ques.split(' ')
        for word in ls_word:
            word = word.strip().strip(',').strip('.')
            if word in feature:
                freq[feature.index(word)] += 1
            else:
                feature.append(word)
                freq.append(1)
                
    return feature, [f/ls_ques.__len__() for f in freq]


def get_ques_feature(ques):
    feature = list()
    freq = list()
    
    ls_word = preprocessing(ques).strip().split(' ')
    for word in ls_word:
        word = word.strip().strip(',').strip('.')
        if word in feature:
            freq[feature.index(word)] += 1
        else:
            feature.append(word)
            freq.append(1)
                
    return feature, freq


def append_feature(src, add):
    new_feature = list()
    new_freq = list()
    
    for idx, feature in enumerate(src[0]):
        if feature not in add[0]:
            new_feature.append(feature)
            new_freq.append(src[1][idx])
        else:
            new_feature.append(feature)
            new_freq.append((src[1][idx] + add[1][add[0].index(feature)]) / 2)
    
    for idx, feature in enumerate(add[0]):
        if feature not in new_feature:
            new_feature.append(feature)
            new_freq.append(add[1][idx])
            
    return new_feature, new_freq


def display_dataframe(Node):
    df = pd.DataFrame([Node.get_feature()[1]],columns=Node.get_feature()[0])
    display(df)


def build_feature(Node, Path):
    if Node.get_child() == None:
        return extract_feature(Path + '\\' + Node.get_name() + '.txt')
    
    feature = [[]]
    for child in Node.get_child():
        child.set_feature(build_feature(child, Path + '\\' + child.get_name()))
        feature = append_feature(feature, child.get_feature())
    
    Node.set_feature(feature)
    return Node.get_feature()


def KNN(ques, Node):
    
    whole = [0]*Node.get_feature()[0].__len__()
    ques_feature = get_ques_feature(ques)
    
    x_test = list(whole)
    for idx, feature in enumerate(ques_feature[0]):
        if feature in Node.get_feature()[0]:
            x_test[Node.get_feature()[0].index(feature)] = ques_feature[1][idx]

    x_train = list()
    y_train = list()
    for child in Node.get_child():
        child_feature = list(whole)
        y_train.append(child.get_name())
        for idx, feature in enumerate(child.get_feature()[0]):
            if feature in Node.get_feature()[0]:
                child_feature[Node.get_feature()[0].index(feature)] = child.get_feature()[1][idx]
        x_train.append(child_feature)

    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    
    knn = KNeighborsClassifier(n_neighbors=1)

    knn.fit(x_train, y_train)
    
    y_pred = knn.predict([x_test])
    
    for child in Node.get_child():
        if child.get_name() == y_pred:
            return child


def intend(ques, Node, Path):
    if Node.get_child() == None:
        return Path + '\\' + Node.get_name() + '.txt'
    
    choose = KNN(ques, Node)
    return intend(ques, choose, Path + '\\' + choose.get_name())


def check_match(p1, p2):
    ls_word1 = p1.split(' ')
    ls_word2 = p2.split(' ')
    
    count_match = 0
    for word in ls_word1:
        if word in ls_word2:
            count_match += 1
    
    return count_match


def ans(ques, file_path):
    ls_ques = get_ls_ques(file_path)
    ls_ans = get_ls_ans(file_path)
    
    ques = ques.strip().strip('?')
    
    max_match = -1
    min_ques = 1000
    ans = ''
    
    for idx, q in enumerate(ls_ques):
        match_point = check_match(ques, q)
        
        if max_match < match_point or (min_ques < len(q) and max_match == match_point) :
            max_match = match_point
            ans = ls_ans[idx].strip()
            min_ques = len(q)
   
    return ans


def main():
    make_ontology()
    build_feature(TDTU, 'data\\TDTU')
        
    while True:
        print('Question: ', end='')
        ques = input()
        if ques == 'quit':
            break
        subject = intend(ques, TDTU, 'data\\TDTU')
        print(subject)
        
        print('Answer: ' + ans(ques, subject))
        print()
    
if __name__ == '__main__':
    main()
