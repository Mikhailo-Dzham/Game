import random


def randominus(a, start=10) -> int: #Видає характеритику
    finish = start
    a = 100 // a - 1
    while True:
        r = random.randint(0, a)
        if r == 1:
            finish += 1
        else:
            break
    return finish


def char_display(teg):
    val = characters[teg]
    print("Сумарні стати: ", val[6], "  Талант: ", val[0] / 10)
    print("PWR: ", val[1], "STM: ", val[2], "HP: ", val[3], "INT: ", val[4], "MP: ", val[5])


def find_top_n_values_with_keys(dictionary, n):
    top_n = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:n]

    for key, value in top_n:
        print(f"Тег: {key % 10_000_000}, Загальні стати: {value}")


chance = 50
spins = 1_000_000
raund = 0
characters = []
teg_stats = {}
counter = 0
for i in range(10_000_000 + raund * spins, 10_000_000 + (raund + 1) * spins):
    character = []
    for j in range(6):
        character.append(randominus(chance))
    stats_sum = sum(character, -character[0])
    character.append(stats_sum)
    characters.append(character)
    teg_stats[i] = stats_sum

find_top_n_values_with_keys(teg_stats, 10)

q = 0
while True:
    q = input()
    if q == 'a':
        with open('archive.txt', 'a') as f:
            for char in characters:
                f.write(" ".join(map(str, char)) + "\n")
    elif q == 'e':
        break
    elif q == 'i':
        with open('teg_sum_stats', 'w') as f:
            for kay in teg_stats.keys():
                f.write(f"{teg_stats[kay]} ")
    elif int(q) >= 0:
        char_display(int(q))
