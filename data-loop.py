student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for e in student:
    if e["score"] >= 80:
       for key,value in e.items():
           print(key,value,'Grade 4')
    elif e["score"] >= 70:
       for key,value in e.items():
           print(key,value,'Grade 3')
    elif e["score"] >= 60:
       for key,value in e.items():
           print(key,value,'Grade 2')
    elif e["score"] >= 50:
       for key,value in e.items():
           print(key,value,'Grade 1')
    else:
       for key,value in e.items():
           print(key,value,'Grade 0')
#นายกัณฑ์อเนก ทรงแสงธรรม 13 6/14