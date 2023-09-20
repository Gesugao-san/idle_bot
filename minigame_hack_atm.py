#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, sys


allowed_values = []
roof_len = 0
allowed_values_roof = [4, 6]
nums = {
    'exist': [],
    'dub': 4,
    'not_meeted_yet': list(range(0, (9 + 1))),
    'not': []
}
user_answer = {
    4: [
        '?',
        '?',
        '?',
        '?'
    ],
    6: [
        '?',
        '?',
        '?',
        '?',
        '?',
        '?'
    ]
}



def line():
    return print('='*10)

def gen_allowed_user(a = 0, b = 9):
    return list(range(a, (b + 1)))

def gen_allowed_bot(a = 0, b = 9):
    return ['X', '0', '_']

def check_input_user(data, _list):
    if data in ['break', 'b', 'stop', 's']:
        exit(0)
    if data in list(_list):
        return True
    return False

def check_input_bot(data, list):
    if data in ['break', 'b', 'stop', 's']:
        exit(0)
    if data in list(list):
        return True
    return False


def meet_num(num, list):
    if num in list:
        list.remove(num)

def num_list_update(num, list):
    if (num not in list):
        list.append(num)

def is_num_on_place(num):
    return (num == 'X')

def is_num_present(num):
    return (num == '0')

def is_num_not_present(num):
    return (num == '_')


def logic(data1, data2, roof):
    if len(data1) != roof:
        print('Error: Invalid data length.')
        return False
    data1_list = list(data1)
    data2_list = list(data2)
    pos = 0
    for i in data1_list:
        i = int(i)
        meet_num(i, nums['not_meeted_yet'])
        if is_num_on_place(data2_list[pos]):
            num_list_update(i, nums['exist'])
            user_answer[roof_len][pos] = i
        if is_num_present(data2_list[pos]):
            num_list_update(i, nums['exist'])
        if is_num_not_present(data2_list[pos]):
            num_list_update(i, nums['not'])
        pos += 1
    nums['dub'] = roof_len - len(nums['exist']) + len(nums['not_meeted_yet'])
    nums['exist'].sort()
    nums['not'].sort()
    print('Final answer:', ''.join(str(user_answer[roof_len])), '| Numbers:', nums)
    return


def main():
    while True:
        try:
            user_input = input('1. You: ')
            if not check_input_user(user_input, allowed_values_user):
                print('Invalid user input', user_input, allowed_values_user)
                continue
            bot_answer = input('2. Bot: ')
            if not check_input_bot(bot_answer, allowed_values_bot):
                print('Invalid bot input', bot_answer, allowed_values_bot)
                continue
            logic(user_input, bot_answer, roof_len)
        except KeyboardInterrupt:
            print('\nInterrupted')
            try:
                sys.exit(130)
            except SystemExit:
                exit(130)
        #except Exception:
        #    print('Exception')
    return



if __name__ == '__main__':
    print('run')
    line()

    allowed_values_user = gen_allowed_user()
    allowed_values_bot = gen_allowed_bot()
    print('allowed_values:', allowed_values)
    print('nums:', nums)

    roof_len = int(input('input roof_len (4, 6): ')) | 0
    if roof_len not in allowed_values_roof:
        print('Error: Invalid roof_len.')
        exit(1)

    print('input loop started')
    print('help: for exit print [b]reak, [s]top or press Ctrl+C.')
    main()

    line()
    print('stop')
    exit(0)




