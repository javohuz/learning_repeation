
"""                          amalyot                                       """

def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
            return b
        else:
            return c
        
def title_string(*matnlar):
    matns = []
    for matn in matnlar:
        matns.append(matn) 
    return [title_str.title() for title_str in matns]

def juft_son(*numbers):
    return [ a for a in numbers if a%2==0 ]

def fibonachchi(a,b,c,d):
    if a+b==c and b+c==d:
        n=True
    else:
        n=False
    return n

