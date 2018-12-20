import pandas as pd
import numpy as np

# 데이터가 있는 엑셀 파일 읽어오는 코드
df = pd.read_excel('movie.xlsx',sheet_name='sheet0')
print(df)

# 컬럼명 확인
df.columns

# 데이터 입력하기 전에 어떤 항목이 있고, 그것을 어떻게 입력을 해야되는지 알려주는 것
print("*********************************************************************************************************")
print("[영화명, 감독, 개봉일, 영화형태, 국적, 전국스크린수, 전국매출액, 전국관객수, 장르, 등급]")
print("중 1개 이상 검색어를 입력하세요.\n")
print("# 영화형태 :〔 단편, 옴니버스, 장편 〕중 검색하세요.")
print("# 장    르 :〔 SF, 가족, 공연, 공포, 다큐멘터리, 드라마, 멜로/로맨스, 뮤지컬, 미스터리, 범죄, 사극,")
print("                서부극, 성인물, 스릴러, 애니메이션, 액션, 어드벤처, 전쟁, 코미디, 판타지 〕중 검색하세요.")
print("# 등    급 :〔 12세관람가, 12세이상관람가, 15세관람가, 15세이상관람가, 18세관람가, 기타, 전체관람가,")
print("                제한상영가, 청소년관람불가 〕 중 검색하세요.")
print("*********************************************************************************************************")

# 영화명을 movie_name_list를 생성하여 거기에 데이터를 받은 후 저장하는 코드
movie_name_list = []
movie_name_list = df['영화명']

# 영화형태을 movie_type_list를 생성하여 거기에 데이터를 받은 후 저장하는 코드
movie_type_list = []
movie_type_list = df['영화형태']

# 국적을 movie_country_list를 생성하여 거기에 데이터를 받은 후 저장하는 코드
movie_country_list = []
movie_country_list = df['국적']

# 장르를 genre_list를 생성하여 거기에 데이터를 받은 후 저장하는 코드
genre_list = []
genre_list = df['장르']

# 등급을 movie_age_list를 생성하여 거기에 데이터를 받은 후 저장하는 코드
movie_age_list = []
movie_type_list = df['등급']

# 영화명을 입력 받아서 1차원 행렬을 다차원 행렬로 변환해주는 코드
def call_movie_name() :
    a_list =[]
    a = ''
    a = input("영화제목을 입력하세요 :")
    a_list = a.split()
    A = np.array(a_list)
#    print("A =", A)
#    print("A.ndim =",A.ndim)
#    print("A.shape =",A.shape)
    print("\n")
    no1 = A.ndim
    no2 = A.shape[0]

    A.shape = no2, no1

    # 검색어를 입력 받아 영화명 컬럼에서 일치하는 값을 찾는 코드
    for X1 in range(0, len(a_list)):
        for Y1 in range(0, 12752):
            answer = df.at[Y1, '영화명']
            if A[X1] == answer:
                print(df.loc[[Y1]])
    return

# 영화형태를 입력 받아서 1차원 행렬을 다차원 행렬로 변환해주는 코드
def call_movie_type() :
    b_list =[]
    b = ''
    b = input("영화형태를 입력하세요 :")
    b_list = b.split()
    B = np.array(b_list)
#    print("B.ndim =",B.ndim)
#    print("B.shape =",B.shape)
#    print("B =",B)
    print("\n")
    no3 = B.ndim
    no4 = B.shape[0]

    B.shape = no4, no3

    # 검색어를 입력 받아 영화형태 컬럼에서 일치하는 값을 찾는 코드
    for X2 in range(0, len(b_list)):
        for Y2 in range(0, 12752):
            answer = df.at[Y2, '영화형태']
            if B[X2] == answer:
                print(df.loc[[Y2]])
    return

# 국적을 입력 받아서 1차원 행렬을 다차원 행렬로 변환해주는 코드
def call_movie_country() :
    c_list =[]
    c = ''
    c = input("국적을 입력하세요 :")
    c_list = c.split()
    C = np.array(c_list)
    print("\n")
    no5 = C.ndim
    no6 = C.shape[0]

    C.shape = no6, no5

    # 검색어를 입력 받아 국적 컬럼에서 일치하는 값을 찾는 코드
    for X3 in range(0, len(c_list)):
        for Y3 in range(0, 12752):
            answer = df.at[Y3, '국적']
            if C[X3] == answer:
                print(df.loc[[Y3]])


    return

# 장르를 입력 받아서 1차원 행렬을 다차원 행렬로 변환해주는 코드
def call_genre() :
    d_list = []
    d = ''
    d = input("장르를 입력하세요 :")
    d_list = d.split()

    D = np.array(d_list)
    print("\n")
    no7 = D.ndim
    no8 = D.shape[0]

    D.shape = no8, no7

    # 검색어를 입력 받아 장르 컬럼에서 일치하는 값을 찾는 코드
    g = 0
    flag = g
    for X4 in range(0,len(d_list)) :
        for Y4 in range(0,12752):
            answer = df.at[Y4, '장르']
            if D[X4] == answer :
                print(df.loc[[Y4]])
        if flag == g :
            print("없음")
    return


# 등급을 입력 받아서 1차원 행렬을 다차원 행렬로 변환해주는 코드
def call_movie_age() :
    e_list =[]
    e = ''
    e = input("등급을 입력하세요 :")
    e_list = e.split()
    E = np.array(e_list)
#    print("E.ndim =",E.ndim)
#    print("E.shape =",E.shape)
#    print("E =",E)
    print("\n")
    no9 = E.ndim
    no10 = E.shape[0]

    E.shape = no10, no9

    # 검색어를 입력 받아 등급 컬럼에서 일치하는 값을 찾는 코드
    for X5 in range(0, 12753):
        #        E[X5]
        #       print(E[X5])
        for Y5 in range(0, 12753):
            if E[X5] == movie_age_list[Y5]:
                print("있음")
            else:
                Y5 = Y5 + 1
    return


# 여러 가지 입력 값 중 어떤 것을 찾을건지 물어보는 코드
question = []
question = input("어떤 것을 찾고 싶으신가요?"
                 "영화명, 영화형태, 국적, 장르, 등급 중 입력하세요. : ")
question_index = ["영화명", "영화형태", "국적", "장르", "등급"]

for r in question_index :
    if question == "영화명" :
        call_movie_name()
    elif question == "영화형태" :
        call_movie_type()
    elif question == "국적" :
        call_movie_country()
    elif question == "장르" :
        call_genre()
    elif question == "등급" :
        call_movie_age()
    else :
        print("찾고 싶은 것을 다시 입력하세요.")
        question = input("어떤 것을 찾고 싶으신가요?"
                         "영화명, 영화형태, 국적, 장르, 등급 중 입력하세요. : ")