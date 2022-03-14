# [Simplify Path] https://leetcode.com/problems/simplify-path/

def simplifyPath(path):
    res = []
    for p in path.split('/'):
        if p == '..':
            if res:
                res.pop()
        elif p and p != '.':
            res.append(p)
    return '/' + '/'.join(res)
