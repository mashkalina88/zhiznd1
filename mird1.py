max_length = int(input('Длина мира'))
mir = []
for i in range(max_length):
    a = input('"+" = живая клетка, "-" = мертвая клетка')
    mir.append(a)
    
new_world = int(input('Сколько рза сгенерировать мир?'))

for j in range(new_world):         
    for i in range(len(mir)):
            if mir[i] == "+" and i < len(mir) - 1:
                if mir[i - 1] == "+" and mir[i + 1] == "+":
                    mir[i] = "-"
                elif mir[i - 1] == "-" and mir[i + 1] == "-":
                    mir[i] = "-"
                
            elif mir[i] == '-' and i < len(mir) - 1:
                if mir[i - 1] == '+' or mir[i + 1] == '+':
                    mir[i] = '+'
    print(mir)
