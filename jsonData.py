import requests
import json
import re




# requests 사용하여서 issues 추출
response = requests.get('http://183.98.121.198:49154//api/v4/issues', headers={"PRIVATE-TOKEN":"H7LJyMarETfnqKbRDpo_"})
reqlist = response.json()                                                   # 가져온 issues api값을 .json()을 이용해서 list형식으로 reqlist변수에 담음
print(len(reqlist))                                                         # reqlist의 index 길이를 확인할 수 있음. 반복문을 돌릴때 많이 사용
print(type(reqlist))                                                        # reqlist의 데이터 타입을 확인가능. 
arr = []                                                                    # 결과값을 가져올 배열선언. 전역변수


i = 0                                                                       # while문을 사용하기 위해 i변수 선언. 인덱스0부터 검색해서 0으로 선언
while i <= len(reqlist):                                                    # reqlist index길이까지 크거가 같을때까지 반복
    if i < len(reqlist):                                                    # reqlist index길이가 크면 false (없는 index에 데이터를 넣어주면 Indexerror 발생)
        id = reqlist[i].get('id')                                           # 반복문을 돌면서 해당 reqlist[i] 인덱스에 .get('id')를 이용해서 id값 추출
        title = reqlist[i].get('title')                                     # 반복문을 돌면서 해당 reqlist[i] 인덱스에 .get('title')를 이용해서 title값 추출
        userid = reqlist[i]['author'].get('id')                             # author 타입은[{}] 리스트안에 딕셔너리형태여서 reqlist[i]['딕셔너리명'].get('created_at')추출
        createdate = reqlist[i].get('created_at')                           # 반복문을 돌면서 해당 reqlist[i] 인덱스에 .get('created_at')를 이용해서 created_at값 추출
        print("createdate : ", createdate)                                  # 결과값 :  2022-08-07T12:10:20.409Z
        yearlist = re.search('([0-9]+)',createdate)                         # re.search 사용해서 0~9 숫자만 추출 - 전까지 2022
        year = yearlist.group()                                             # search 결과값을 .group()를 사용하여서 2022를 year 변수에 넣어줌
        print("year : " ,year)                                              # 2022
        url = reqlist[i].get('web_url')                                     # 반복문을 돌면서 해당 reqlist[i] 인덱스에 .get('web_url')를 이용해서 web_url 추출 
        print(url)                                                          # 결과 값 : http://gitlab-gitlab-ce1/
        weburl = url.replace('gitlab-gitlab-ce1', '183.98.121.198:49154')   # url.replace를 사용해서 gitlab-gitlab-ce1 상수 값을 183.98.121.198:49154로 변경


        blankpattern = "([0-9]+)\/([0-9]+)\s\~\s([0-9]+)\/([0-9]+)"         # 예) 08/24 ~ 08/26 정규식패턴를 추출하는 패턴
        noblankpattern = "([0-9]+)\/([0-9]+)\~([0-9]+)\/([0-9]+)"           # 예) 08/24~08/26 정규식패턴를 추출하는 패턴
        strdate = ''                                                        # strdate담을 변수 선언
        enddate = ''                                                        # enddate담을 변수 선언
                                       
        blank = re.search(blankpattern,title)                               # re.search 함수로 title값을 blankpattern 정규식 실행
        noblank = re.search(noblankpattern,title)                           # re.search 함수로 title값을 noblankpattern 정규식 실행
        if blank != None or noblank != None:                                # blank가 None아니거나 noblank가 None아니면 true (or연산자:두조건식중 하나라도 맞으면 true)
            if blank == None :                                              # blank()가 None이면 true 
                dateresult = noblank.group()                                # 정규식 결과값 변수 담음. 
                print('dateresult ',dateresult)                             # 결과 값 : 예) 08/24~08/25
                date = dateresult.split('~')                                # split 함수로 '~'로 잘라서 리스트로 반환 ( date[0] = 08/24 , date[1] = 08/25)          
                strdate = year+'-'+date[0].replace('/','-')                 # strdate = year(2022)+'-'+date[0](08/24).replace('/','-')(08-24) 합친 값:2022-08-24
                enddate = year+'-'+date[1].replace('/','-')                 # enddate = year(2022)+'-'+date[1](08/25).replace('/','-')(08-25) 합친 값:2022-08-25    
                      
            else :
                dateresult = blank.group()                                  # 정규식 결과값 변수 담음.
                print('dateresult ',dateresult)                             # 결과 값 : 예) 08/24 ~ 08/25
                date = dateresult.split(' ~ ')                              # split 함수로 ' ~ '로 잘라서 리스트로 반환 ( date[0] = 08/24 , date[1] = 08/25)          
                strdate = year+'-'+date[0].replace('/','-')                 # strdate = year(2022)+'-'+date[0](08/24).replace('/','-')(08-24) 합친 값:2022-08-24
                enddate = year+'-'+date[1].replace('/','-')                 # enddate = year(2022)+'-'+date[1](08/25).replace('/','-')(08-25) 합친 값:2022-08-25    

        jsondic= {}                                                         # 딕셔너리 선언 
            
        jsondic['id'] = id                                                  # jsondic['변수이름'] = id  key : value 형태로 데이터를 담음
        jsondic['title'] = title
        jsondic['url'] = weburl
        jsondic['start'] = strdate
        jsondic['end'] = enddate
        jsondic['userid'] = userid

        print(jsondic)                                                      
        arr.append(jsondic)                                                 # 값이 담겨진 딕셔너리를 arr이라는 리스트에 담음. (arr.append)
        
        

    else :                                                                  # if문 else 구문
        break                                                               # reqlist index길이까지 크거가 같으면 while문 break
    i += 1                                                                  # while문 제일 마지막 실행부분 변수 i값을 +1해주는 로직

print("result : ",arr)                                                      # 리스트에 담겨있는 딕셔너리 결과 값 [{}]
   

with open("events.json","w", encoding="UTF-8") as f:                        # open("파일이름", "w"(쓰기)) as f :
    json.dump(arr,f ,ensure_ascii=False)                                    # 가공된 데이터를 json.dump()안에 넣어주면 events.json() 파일이 생성











