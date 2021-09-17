#!/usr/bin/env python
# coding: utf-8

# # Decision Tree 

# In[1]:
from math import log


class Cube:
    def __init__(self, table, cond):
        self.table = table
        self.cond = cond

    def get_value(self):
        return self.table

    def get_cond(self):
        return self.cond


# In[2]:


def entropy_table(table):
    """
        table: two dimensional array [[]]
        out put: An int value that calculate by e(S) = - p/(p + q)*log(p/(p + q), 2) - q/(p + q)*log(q/(p + q), 2)
    """
    Entropy = 0
    ls_e = list()
    for i in table[-1][1:]:
        if i not in ls_e:
            ls_e.append(i)
            Entropy += - table[-1].count(i) / (len(table[0]) - 1) * log(table[-1].count(i) / (len(table[0]) - 1), 2)
    return Entropy


# In[3]:


def new_table(label, table):
    """
        label: string
        table: [[]]
        output: new table fit with label
    """
    src = list()
    for row in table:
        if label in row:
            src = row
            break

    new = [[]]
    for row in table:
        if row[0] != src[0]:
            tmp2 = [row[0], ]
            for i in range(src.__len__()):
                if src[i] == label:
                    tmp2.append(row[i])
            new.append(tmp2)

    return new[1:]


# In[4]:


def gain_table(e, table):
    """
        e: float value
        table: two dimensional array [[]]
        output: Label of Vi that have max Gain(e, V) value
    """
    V_imax = ''
    max_gain = 0
    val = list()
    for row in table[:-1]:
        sum_e = 0
        for label in row[1:]:
            if label not in val:
                val.append(label)
                sum_e += row.count(label) / (row.__len__() - 1) * entropy_table(new_table(label, table))
        if max_gain < e - sum_e:
            max_gain = e - sum_e
            V_imax = row[0]
    return V_imax


# In[5]:


def divide_table(t, lable):
    """
        label: an string
        t: a class table
        output: a list of class that contain new tables
            - set condition and new tables value
            - condition is inheritance (condition = t.cond() + ', ' + label + ':' + V)
    """
    tables = list()
    table = t.get_value()
    cond = t.get_cond()

    src = list()
    for row in table:
        if lable in row:
            src = row
            break

    added = list()
    for V in src[1:]:
        if V not in added:
            added.append(V)
            new_cube = Cube(new_table(V, table), cond + ', ' + lable + ': ' + V)
            tables.append(new_cube)

    return tables


# In[6]:


def decision_tree(initial):
    """
        initial: table with full data
        output: dictionary contain conditions
        Use Queue:
            - Push Cube(initial) to Queue
            - Get first value of Queue and set to variable t
            - if e(t) == 0: add to dict
            - else: divive t to piece (with label) and add to Queue
            * Cube: class
            * divive to piece depend on gain value
    """
    cond = {}
    tables = [Cube(initial, ''), ]
    for t in tables:
        E = entropy_table(t.get_value())
        if E == 0:
            cond[t.get_cond().strip(', ')] = t.get_value()[-1][1]
        else:
            label = gain_table(E, t.get_value())
            next_table = divide_table(t, label)
            tables.extend(next_table)
    return cond


# In[7]:


def load_data():
    """
        input: ...
    """
    filename = 'dataDT.txt'
    return [[j for j in i.split(', ')] for i in open(filename, 'r').read().split('\n')]


# In[8]:


def load_test():
    """
        input: ...
    """
    return 'Quoc tich: Y, Gia canh: Doc than'


# In[9]:


def is_in_set(set_a, set_b):
    for item in set_a:
        if item not in set_b:
            return False
    return True


# In[10]:


def test(condition_tree):
    #     need fix`
    test_set = load_test().split(', ')
    for cond in condition_tree:
        if is_in_set([cond], test_set):
            print(condition_tree[cond])


# In[14]:


def main():
    condition_tree = decision_tree(load_data())
    #     test(condition_tree)
    for path in condition_tree:
        print(path)


if __name__ == '__main__':
    main()

# In[15]:


load_data()

# In[ ]:
