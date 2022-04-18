file = open('words.txt', 'r')

first = {}
second = {}
third = {}
fourth = {}
fifth = {}
word_count = 0

lines = file.readlines()
for line in lines:
    word = line.strip()
    word_count += 1

    for i in range(len(word)):
        if i == 0:
            if word[i] in first:
                first[word[i]] += 1
            else:
                first[word[i]] = 1
        elif i == 1:
            if word[i] in second:
                second[word[i]] += 1
            else:
                second[word[i]] = 1
        elif i == 2:
            if word[i] in third:
                third[word[i]] += 1
            else:
                third[word[i]] = 1
        elif i == 3:
            if word[i] in fourth:
                fourth[word[i]] += 1
            else:
                fourth[word[i]] = 1
        elif i == 4:
            if word[i] in fifth:
                fifth[word[i]] += 1
            else:
                fifth[word[i]] = 1

# given a partial word, the greatest possibility of a word being a valid word
# base case: if only one unknown letter

total = {}
for key in first:
    total[key] = first[key]

for key in second:
    total[key] += second[key]

for key in third:
    total[key] += third[key]

for key in fourth:
    total[key] += fourth[key]

for key in fifth:
    total[key] += fifth[key]

data_sorted = {k: v for k, v in sorted(total.items(), key=lambda x: x[1])}
print(data_sorted)

max_probability = 0
max_word = ''

for line in lines:
    word = line.strip()
    temp_probability = 1
    temp_probability *= first[word[0]] / word_count
    temp_probability *= second[word[1]] / word_count
    temp_probability *= third[word[2]] / word_count
    temp_probability *= fourth[word[3]] / word_count
    temp_probability *= fifth[word[4]] / word_count
    if temp_probability > max_probability:
        max_probability = temp_probability
        max_word = word


print(max_word)
print(max_probability)

'''
absent: list
inplace: list of length 5
wrong_place: list of length 5
'''
def filter(absent: list, inplace: list, wrong_place: list):
    w = ''
    max_probability = 0
    for line in lines:
        word = line.strip()
        # not containing any letter in absent
        if (word[0] not in absent) and (word[1] not in absent) and (word[2] not in absent) and (word[3] not in absent) and (word[4] not in absent):
            qualified = True
            # inplace letters must be in the right place
            for i in range(len(inplace)):
                if inplace[i] == '':
                    continue
                elif word[i] != inplace[i]:
                    qualified = False
                    break

            # letters must be contained and in wrong_place
            for i in range(len(wrong_place)):
                if wrong_place[i] == '':
                    continue
                elif wrong_place[i] not in word or wrong_place[i] == word[i]:
                    qualified = False
                    break

            if qualified:
                temp_probability = 1

                if (inplace[0] == ''):
                    temp_probability *= first[word[0]] / word_count
                
                if (inplace[1] == ''):
                    temp_probability *= second[word[1]] / word_count

                if (inplace[2] == ''):
                    temp_probability *= third[word[2]] / word_count

                if (inplace[3] == ''):
                    temp_probability *= fourth[word[3]] / word_count

                if (inplace[4] == ''):
                    temp_probability *= fifth[word[4]] / word_count

                if temp_probability > max_probability:
                    max_probability = temp_probability
                    w = word
    print(w)
    return w


a = ['s', 'o', 'e', 'p', 't', 'y', 'b', 'i', 'd', 'l', 'f']
i = ['', 'r', 'a', 'c', 'k']
w = ['c', '', '', 'r', '']

filter(a, i, w)


# same letter multiple times
#  letter that are inplace cannot be added to absent
#  instead, they must be ignored from the dict

# should not use a list for wrong_place, since there may be multiple wrong_place letters for a position

# best first word search
# input optimization