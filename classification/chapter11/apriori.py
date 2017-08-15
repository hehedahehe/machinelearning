#coding:utf-8

# c 项集的集合
# l 频繁项集的集合
# c=>l=>ci=>li


# 关联规则算法：
# 1. 首先通过apriori算法获取频繁项集
# 2. 依据频繁项集获取关联规则

def load_data():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def gen_c1(data):
    '''
    得到c1项集
    :param data:
    :return:
    '''
    c1 = []
    transactions = data
    for transaction in transactions:
        for item in transaction:
            if [item] not in c1:
                c1.append([item])
    c1.sort()
    return list(map(frozenset, c1))  # python3
    # return map(frozenset, c1)# python2


def scan_d(transactions, ck, data_support, min_support,):
    '''
    ck项集对D进行扫描，返回lk，即从ck中获取频繁项集
    :param transactions:
    :param ck:
    :param min_support:
    :return:
    '''
    #统计出现次数
    data_support_count = {}
    for transaction in transactions:
        for c in ck:
            if c.issubset(transaction):
                if c not in data_support_count:
                    data_support_count[c] = 1
                else:
                    data_support_count[c] += 1
    lk = []
    #过滤掉非频繁项
    nums = float(len(transactions))
    for key in data_support_count:
        if key not in data_support:
            data_support[key] = data_support_count[key]/nums
        if data_support[key] >= min_support:
            lk.append(key)

    return lk




def get_ck(l_previous):
    '''
    由k-1频繁项集获取ck项集
    比如说由l2获取c3
    :param l_previous:k-1频繁项集
    :return:
    '''
    ck = []
    k = len(l_previous[0]) + 1
    l_l_previous = len(l_previous)
    for i in range(0, l_l_previous):
        for j in range(i+1, l_l_previous):
            l1 = list(l_previous[i])[:k-2]
            l2 = list(l_previous[j])[:k-2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                ck.append(l_previous[i]|l_previous[j])
    return ck

def apriori(dataset, min_support):
    data_support = {}
    k_max = 3
    l_all = []
    c1 = gen_c1(dataset)
    l1 , _ = scan_d(dataset, c1,data_support, min_support)
    l = l1
    while(k_max>0):
        c = get_ck(l)
        l, _ = scan_d(dataset, c, data_support, min_support)
        if l:
            l_all.append(l)
        else:
            break
        k_max -= 1
    return l_all

def gen_rules(li, support_data, min_conf, min_support):
    '''
    从一个频繁项集中获取规则
    核心是找到P, H, 计算support(P|H)/support(P)  P->H
    计算核心：
    {1,2,3,4}从中找到所有的规则P->H，进行计算其置信系数，（前提是P和H是频繁项集）
    :param li: 一个频繁项，例如 {1,2,3,4}
    :param support_data: 项集的支持度数据
    :param min_conf: 置信系数
    :return: 满足置信系数的规则
    '''
    ln = len(li)
    association_items = [] # [(),(),()]
    k = 2
    association_items.extend(get_k_group(li, k))
    for item in association_items:
        a_b, b_a = get_confidence(item, support_data)
        print(str(item[0])+"==>"+str(item[1])+"=="+str(a_b))
        print(str(item[1])+"==>"+str(item[0])+"=="+str(b_a))


def get_confidence(item_pair, support_data):
    union_pair = item_pair[0].union(item_pair[1])
    support_union = support_data[union_pair]
    support_a = support_data[item_pair[0]]
    support_b = support_data[item_pair[1]]
    a_b = support_union/support_a
    b_a = support_union/support_b
    return a_b, b_a

def get_k_group(arr, k):
    '''
    获取CnK的所有组合情况
    :param arr: 输入的集合,是一个frozenset
    :param k: 元组大小
    :return: 所有的元组的集合
    '''
    res = []
    arr1 = list(arr)
    length = len(arr)
    step = k - 1
    for i in range(length):
        for j in range(i+1,length):
            tmp = []
            tmp.append(arr1[i])
            end = j + step
            if end <= length:
                tmp.extend(arr1[j:end])
                tmp = frozenset(tmp)
                tmp_another = arr - tmp
                res.append((tmp, tmp_another))
    return res

if __name__ == "__main__":
    min_support = 0.5
    data = load_data()
    data_support = {}
    c = gen_c1(data)
    l = scan_d(data,c,data_support, min_support)
    l_all = []
    while True:
        c = get_ck(l)
        l = scan_d(data, c, data_support, min_support)
        if not l:
            break
        else:
            l_all.append(l)


    l_max = [each[0] for each in l_all if len(each[0])==3][0]
    print(l_max)
    gen_rules(li=l_max,support_data=data_support,min_conf=0.2,min_support=min_support)



