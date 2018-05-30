import os, sys
import numpy as np
import pandas as pd

def scoreAUC(labels, probs):
    i_sorted = sorted(range(len(probs)),key=lambda i: probs[i],
                      reverse=True)
    auc_temp = 0.0
    TP = 0.0
    TP_pre = 0.0
    FP = 0.0
    FP_pre = 0.0
    P = 0
    N = 0
    last_prob = probs[i_sorted[0]] + 1.0
    for i in range(len(probs)):
        if last_prob != probs[i_sorted[i]]: 
            auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0        
            TP_pre = TP
            FP_pre = FP
            last_prob = probs[i_sorted[i]]
        if labels[i_sorted[i]] == 1:
            TP = TP + 1
        else:
            FP = FP + 1
    auc_temp += (TP+TP_pre) * (FP-FP_pre) / 2.0
    auc = auc_temp / (TP * FP)
    return auc


def validate(submit_file, test_file, options = True):
    
    lines = open(test_file).readlines()
    data = []
    for line in lines:
        s = line.strip('\n').split('\t')
        data.append(s[0] + '_' + s[1])
        #data[s[1] + '_' + s[2]] = int(s[0])

    prob_inrange = True
    lines = open(submit_file).readlines()
    submit_data = []
    for line in lines:
        s = line.strip('\n').split('\t')
        submit_data.append(s[0] + '_' + s[1])
        # print (float(s[2]))
        if not (0 <= float(s[2]) <= 1):
            prob_inrange = False

    data.sort()
    submit_data.sort()

    if data == submit_data and len(data) == len(submit_data) and prob_inrange:

        return {'code': 0, 'message': 'validation success'}
    else:
        return {'code': -1, 'message': 'validation fail'}


def score(submit_file, test_file, options = True):

    lines = open(test_file).readlines()
    data = {}
    for line in lines:
        s = line.strip('\n').split('\t')
        #data.append(s[1] + '_' + s[2])
        data[s[0] + '_' + s[1]] = float(s[2])

    lines = open(submit_file).readlines()
    submit_data = {}
    for line in lines:
        s = line.strip('\n').split('\t')
        submit_data[s[0] + '_' + s[1]] = float(s[2])
    
    labels = []
    probs = []
    for key in data.keys():
        labels.append(data[key])
        probs.append(submit_data[key])

    auc = scoreAUC(labels, probs)

    return {
        'code': 0, 
        'score': auc,
        'message': 'success'
        }

# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print ('usage: python score.py test_file submit_file')
#     test_file = sys.argv[1]
#     submit_file = sys.argv[2]
#     print (validate(submit_file, test_file))
#     print (score(submit_file, test_file))


