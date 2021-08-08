"""
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_txt = {}


def main():
    start = time.time()
    global all_ans
    global ans
    read_dictionary()
    while True:
        ans = ""
        all_ans = []
        print('Welcome to "Anagram Generator" (or' + EXIT + ' to quit)')
        input_w = input('Find anagram for:')
        if input_w == EXIT:
            print('EXIT!')
            break
        else:
            #start = time.time()
            find_anagrams(input_w)
            print(str(len(all_ans)) + ' anagrams:' + str(all_ans))
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dict_txt
    with open(FILE, 'r') as f:
        for vocabulary in f:
            if vocabulary[0:4].strip() not in dict_txt:
                dict_txt[vocabulary[0:4].strip()] = [vocabulary.strip()]
            else:
                dict_txt[vocabulary[0:4].strip()].append(vocabulary.strip())


def find_anagrams(s):
    find_anagrams_helper(s, [], list(range(len(s))))
def find_anagrams_helper(s, current, t):
    global all_ans
    global ans
    if len(s) == len(current):
        if ans[0:4] in dict_txt:
            if ans in dict_txt[ans[0:4]] and ans not in all_ans:
                all_ans.append(ans)
                print('Searching...')
                print('Found: ' + ans)
    else:
        for _ in t:
            current.append(t[0])
            ans += s[t[0]]
            t.remove(t[0])
            if len(ans) > 3:
                if has_prefix(ans):
                    find_anagrams_helper(s, current, t)
            else:
                find_anagrams_helper(s, current, t)
            giveup_num = current.pop()
            t.append(giveup_num)
            str_to_list = list(ans)
            str_to_list.pop()
            ans = ("".join(str_to_list))


def has_prefix(sub_s):
    if sub_s[0:4] in dict_txt:
        for vocabulary in dict_txt[sub_s[0:4]]:
            if vocabulary.startswith(sub_s):
                return True
        return False



if __name__ == '__main__':
    main()
