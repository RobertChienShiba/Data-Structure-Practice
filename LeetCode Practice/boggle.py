"""
File: boggle.py
Adapted from LeetCode 79 Word Search("https://leetcode.com/problems/word-search/")
"""
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    all_ans=[]
    boggle_list=[]
    _dict=read_dictionary()
    for i in range(1,5):
        input_w=input(f"{i} row of letters:")
        input_w_list=input_w.lower().split(" ")
        for letter in input_w_list:
            if len(letter) != 1:
                 print('Illegal input')
                 return None
        boggle_list.append(input_w_list)
    for i in range(len(boggle_list)):
        for j in range(len(boggle_list[0])):
            start_alpha=boggle_list[i][j]
            ##Parameters are Start points,Sequential letter coordinate, 
            ##Letter coordinates have been traversed have been founded words
            find_boggle(start_alpha,[i,j],[(i,j)],boggle_list,_dict,all_ans)
    print(f"There are {len(all_ans)} words in total")


def find_boggle(alpha,current,seen_alpha,boggle_list,_dict,all_ans):
    ##Read the Dict if length longer than four
    if len(alpha) >= 4 :
        all_ans=add_word(alpha, _dict, all_ans)
    ##Find the first dimension coordinate
    for i in range(-1,2):
        if current[0]+i < 0 or current[0]+i >= len(boggle_list):
            continue
        ##Find the second dimension coordinate
        for j in range(-1,2):
            new_idx1 = current[0]+i
            new_idx2 = current[1]+j
            ##Filter itself,out of index and Letter coordinates have been traversedFilter itself,out of index and Letter coordinates have been traversed
            if new_idx2 < 0 or new_idx2 >= len(boggle_list[0]) or (new_idx1,new_idx2) in seen_alpha or (i == 0 and j == 0):
                continue
            ans=alpha+boggle_list[new_idx1][new_idx2]
            if has_prefix(ans,_dict):
                ##move to next letter coordinate
                current=[new_idx1,new_idx2]
                ##Record walked
                seen_alpha.append((new_idx1,new_idx2))
                find_boggle(ans,current,seen_alpha,boggle_list,_dict,all_ans)
                ##return last letter coordinate
                current=[current[0]-i,current[1]-j]
                ##delette the last walked Record
                seen_alpha.pop()
            

def add_word(alpha,_dict,all_ans):
    if alpha in _dict[alpha[0]] and alpha not in all_ans:
        print("Found:"+alpha)
        all_ans.append(alpha)
        return all_ans
    return all_ans

                        
def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dict_txt = {}
    with open(FILE, 'r') as f:
        for vocabulary in f:
            if vocabulary[0].strip() not in dict_txt:
                dict_txt[vocabulary[0].strip()] = [vocabulary.strip()]
            else:
                dict_txt[vocabulary[0].strip()].append(vocabulary.strip())
    return dict_txt

def has_prefix(sub_s,_dict):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for vocabulary in _dict[sub_s[0]]:
        if vocabulary.startswith(sub_s):
          return True
    return False

if __name__ == '__main__':
	main()
