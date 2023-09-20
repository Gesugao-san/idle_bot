#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, sys


allowed_values = []
roof_len = 0
allowed_values_roof = [4, 6]
nums = {
    'exist': [],
    'not': [],
    'not_meeted_yet': list(range(0, (9 + 1)))
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

def gen_allowed(a = 0, b = 9):
    return list(range(a, (b + 1))) + ['X', '0', '_']


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
    nums['exist'].sort()
    nums['not'].sort()
    print('user_answer:', user_answer[roof_len])
    print('nums:', nums)
    return


def main():
    while True:
        try:
            user_input = input('1. (' + str(roof_len) + ') [b]reak, [s]top> ')
            if user_input in ['break', 'b', 'stop', 's']:
                exit(0)
            bot_answer = input('2. (' + str(roof_len) + ') [b]reak, [s]top> ')
            if bot_answer in ['break', 'b', 'stop', 's']:
                exit(0)
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

    allowed_values = gen_allowed()
    print('allowed_values:', allowed_values)
    print('nums:', nums)

    roof_len = int(input('input roof_len (4, 6): ')) | 0
    if roof_len not in allowed_values_roof:
        print('Error: Invalid roof_len.')
        exit(1)

    print('input loop started')
    main()

    line()
    print('stop')
    exit(0)




