# # simple generator
# def my_gen():
#     n = 1 
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#     n += 1
#     print('This is printed second')
#     yield n

#     n+=1
#     print('This is printed at last')
#     yield n


# a = my_gen()

# next(a)
# next(a)
# next(a)
# from operator import ne
# from random import randint
# def enemyAttack():
#     hp = 100
#     count = 1

#     attack = randint(1,20)
#     print('Enemy attacked: ' + str(attack))
#     hp = hp - attack
#     print('your HP: ' + str(hp))
#     yield count

#     count += 1
#     attack = randint(1,20)
#     print('Enemy attacked: ' + str(attack))
#     hp = hp - attack
#     print('your HP: ' + str(hp))
#     yield count

#     count += 1
#     attack = randint(1,20)
#     print('Enemy attacked: ' + str(attack))
#     hp = hp - attack
#     print('your HP: ' + str(hp))
#     yield count


# battle = enemyAttack()

# next(battle)
# next(battle)
# next(battle)


