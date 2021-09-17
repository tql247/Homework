import numpy as np

def get_prob_lable(train, lable):
    '''
    :param train: array, data set for training
    :param lable: String
    :return: int, frequence of label in data
    '''
    return sum([1 for data_i in train if data_i[-1] == lable])/train.__len__()


def get_prob_feature_depend_lable(train, lable):
    '''
    :param train: array, data set for training
    :param lable: String
    :return: list(), frequence of each feature belong with label
    '''
    ls_prob = [0]*(train[0].__len__() - 1)
    for data_i in train:
        if data_i[-1] == lable:
            ls_prob = ls_prob + data_i[:-1].astype(np.int)
            
    return ls_prob


def get_prob_feature(train, test, lable):
    '''
    :param train: array, data set for training
    :param test: list(), test data
    :param lable: String
    :return: list(), list of P(x_i|y)
    '''
    prob_lable = get_prob_lable(train, lable)
    ls_prob_feature_depend_lable = get_prob_feature_depend_lable(train, lable)
    
    train_prob = [prob_feature/prob_lable for prob_feature in ls_prob_feature_depend_lable]
    
    return [train_prob[i]**test[i]*(1 - train_prob[i])**(1 - test[i]) for i in range(len(test))]


def prob(train, test, lable_target):
    '''
    :param train: array, data set for training
    :param test: list(), test data
    :param lable_target: String
    :return: float, predict value of lable_target
    '''
    ls_prob_feature = get_prob_feature(train, test, lable_target)
    P = get_prob_lable(train, lable_target)
    for prob_feature in ls_prob_feature:
        P *= prob_feature
    
    return P

train = np.array([[1, 1, 0, 1, 0, 'N'],
         [0, 1, 1, 0, 0, 'N'], 
         [1, 0, 1, 0, 1, 'S'], 
         [1, 1, 1, 1, 0, 'S'], 
         [0, 1, 0, 1, 0, 'S'], 
         [0, 0, 0, 1, 1, 'N'], 
         [0, 1, 0, 0, 0, 'S'], 
         [1, 1, 0, 1, 0, 'S'], 
         [0, 0, 1, 1, 1, 'N'], 
         [1, 0, 1, 0, 1, 'S']])

def main():
    test = [1, 0, 0, 1, 1]
    p_s = prob(train, test, 'S')
    p_n = prob(train, test, 'N')
    print('Prob of test is S:', end=' ')
    print(p_s/(p_s + p_n))
    print('Prob of test is N:', end=' ')
    print(p_n/(p_s + p_n))

if __name__ == '__main__':
    main()