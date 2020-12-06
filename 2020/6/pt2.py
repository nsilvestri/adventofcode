#!/bin/python
with open('input.txt') as file:
    data = file.read()
    groups = data.split('\n\n')

    for i in range(0, len(groups)):
        groups[i] = groups[i].split('\n')
    
    score_sum = 0
    for group in groups:
        answers = {}
        for person in group:
            for answer in person:
                if answer not in answers:
                    answers[answer] = 1
                else:
                    answers[answer] += 1
        for answer in answers.values():
            if answer == len(group):
                score_sum += 1

    print(score_sum)
    
