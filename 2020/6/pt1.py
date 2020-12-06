#!/bin/python
with open('input.txt') as file:
    data = file.read()
    groups = data.split('\n\n')

    for i in range(0, len(groups)):
        groups[i] = groups[i].split('\n')
    
    score_sum = 0
    for group in groups:
        answers = set()
        for person in group:
            for answer in person:
                answers.add(answer)
        score_sum += len(answers)

    print(score_sum)
    
