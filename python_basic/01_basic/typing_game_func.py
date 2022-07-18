
# 타자게임
# 데이터 저장 : word = []
# word  리스트에서 문제를 추출하여 제출하면 맞추는 게임
# - 한번 출제된 문제는 맞출때까지 반복
# - 전체 5문제를 출제 다 맞추면 종료

import json
import time
import os
import random


def data_load(path):
    f = open(path, 'r')
    word = json.load(f)
    f.close()
    return word

def game(word, rank):
    print('게임시작!')
    start = time.time()
    n = 1
    quiz = random.choice(word)
    while n <= 5:
        print(f'{n}번')
        print(quiz)
        result = input('>>>')
        if quiz == result:
            print('통과!')
            n += 1
            quiz = random.choice(word)
        else:
            print('오타! 다시도전!')
    end = time.time()
    print(f'걸린 시간 : {end-start:.0f}초')
    name = input('이름을 입력하세요 >>>')
    rank={}
    rank[name] = end-start
    print(rank)

def quiz_add(word):
    print('문제추가작업')
    while True:
        data = input('(종료:enter) >>>')
        if data == '':
            break
        word.append(data)
    print(word)

def data_save(path,data):
    print('저장작업')
    f = open(path,'w')
    json.dump(data,f)
    f.close()
    
def rank_list(rank):
    print('등수리스트')
    for index,(k,v) in enumerate(sorted(rank.items(),key=lambda x : x[1])):
        print(f'{index+1}등 {k} 시간:{v:.2f}')

def quit_save():
    print('프로그램 종료!')
    