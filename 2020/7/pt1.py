#!/bin/python

containers_of_bags = {}

containing_bags = set()
def bags_containing(contained):
    print(contained + ' bags are contained by: ' + str(containers_of_bags[contained]))
    for bag in containers_of_bags[contained]:
        containing_bags.add(bag)
        containing_bags.union(bags_containing(bag))
    return containing_bags


with open('input.txt') as file:
    for line in file:
        tokens = line.strip().split(' bags contain ')
        container_bag = tokens[0]
        # required for root bag
        if container_bag not in containers_of_bags:
            containers_of_bags[container_bag] = [] 

        # get a list of contained bags with colors
        contained_bags = tokens[1].replace('.', '')
        contained_bags = contained_bags.split(', ')
        contained_bags = [bag[2:] for bag in contained_bags]
        contained_bags = [' '.join(bag.split(' ')[0:2]) for bag in contained_bags]

        # add containers for each bag
        for bag in contained_bags:
            if bag not in containers_of_bags:
                containers_of_bags[bag] = []
            containers_of_bags[bag].append(container_bag)
    
    print(bags_containing('shiny gold'))
    print(len(bags_containing('shiny gold')))