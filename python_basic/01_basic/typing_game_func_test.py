
# 타자게임
# 데이터 저장 : word = []
# word  리스트에서 문제를 추출하여 제출하면 맞추는 게임
# - 한번 출제된 문제는 맞출때까지 반복
# - 전체 5문제를 출제 다 맞추면 종료

import typing_game_func as tf
import os

path = os.path.dirname(__file__)
word = tf.data_load(path+'/word.json')
rank = tf.data_load(path+'/rank.json')

menu_display = '''
------------------------------------------------------
1.게임   2.문제추가  3.문제저장 4.등수리스트  5.종료
------------------------------------------------------
>>> '''

while True:
    menu = input(menu_display)
    if menu == '1':
        tf.game(word,rank)    
    elif menu == '2':
        tf.quiz_add(word)
    elif menu == '3':
        tf.data_save(path+'/word.json',word)
        tf.data_save(path+'/word.json',rank)
    elif menu =='4':
        tf.rank_list(rank)
    elif menu == '5':
        tf.data_save(path+'/word.json',word)
        tf.data_save(path+'/word.json',rank)
        tf.quit_save()
        break
    else:
        print('메뉴를 선택하셨습니다.')

