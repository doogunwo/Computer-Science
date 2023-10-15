from collections import deque




def find(subway,start,end,path=[]):
    
    path = path + [start]
    if start == end:
        return path
    if start not in subway:
        return None
    short_path = None
    for station in subway[start]:
        if station not in path:
            new  = find(subway,station,end,path)
            if new :
                if not short_path or len(new) < len(short_path):
                    short_path = new
    return short_path
            
subway = {
    #1호선 위
    "노포" : ['범어사'],
    '범어사' : ['노포','남산'],
    '남산' : ['범어사','두실'],
    '두실' : ['남산','구서'],
    '구서' : ['두실','장전'],
    '장전' : ['구서','부산대'],
    '부산대' : ['장전','온천장'],
    '온천장' : ['부산대','명륜'],
    '명륜' :['온천장', '동래'],
    '동래' : ['명륜','교대'],
    '연산' : ['동래','시청'],
    '시청' : ['연산','양정'],
    '양정' :['시청','부전'],
    '부전' : ['양정','서면'],
    '서면' : ['부전','범내골','부암','전포'],
    #2호선 좌측
    '부암' : ['가야','서면'],
    '가야' : ['동의대','부암'],
    '동의대' :['개금','가야'],
    '개금' : ['냉정','동의대'],
    #2호선 우측
    '전포' : ['서면','국제금융센터'],
    '국제금융센터' :['전포','문현'],
    '문현' : ['국제금융센터','지게골'],
    #1호선 아래
    '범내골' : ['서면','범일'],
    '범일' : ['범내골','좌천'],
    '좌천' : ['범일','부산진']  
 }


start, end = input().split()
res = find(subway,start,end)
print(res)
