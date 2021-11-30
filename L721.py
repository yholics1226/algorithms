# [Accounts Merge] https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
def accountsMerge(accounts):
    def find(v):
        if mails[v] == v:
            return v
        else:
            mails[v] = find(mails[v])
            return mails[v]
    def union(a, b):
        fa = find(a)
        fb = find(b)
        if fa != fb:
            del m2i[fb]
            mails[fb] = fa
        return fa
    m2i = dict()
    mails = dict()
    for acc in accounts:
        if len(acc) == 2:
            if acc[1] not in mails:
                mails[acc[1]] = acc[1]
                m2i[acc[1]] = acc[0]
        else:
            for i in range(2, len(acc)):
                a, b = acc[i-1], acc[i]
                if a not in mails:
                    mails[a] = a
                    m2i[a] = acc[0]
                if b not in mails:
                    mails[b] = a
                union(a, b)
    res = defaultdict(list)
    for mail in mails:
        res[find(mail)].append(mail)
    ans = [[m2i[x]] + sorted(res[x]) for x in m2i]
    return ans
