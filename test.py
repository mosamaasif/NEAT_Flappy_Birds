from main import *

for i in range(1, 7): 
    lines = None
    with open('config-feedforward.txt', 'r') as file:
        lines = file.readlines()
    
    if lines is not None:
        lines[3] = f'pop_size              = {i * 10}\n'
        with open('config-feedforward.txt', 'w') as file:
            file.writelines(lines)
        best, gen = main_func()

        with open(f'p{i * 10}.txt', 'w+') as file:
            file.writelines(f'GEN: {gen}\n{best}')