# не могу сообразить как зациклить, так как исходная переменная меняется ежедневно. Ведь спортсмен каждый день улучшает результат на 10%, а значит меняется ежедневно исходная "а"
print('Привет, мой любимый спортсмен! Ты очень моного занимаешься и я хочу помочь тебе улучшить твой результат! Давай посчитаем сколько дней тебе понадобиться, что бы достичь своей цели! Учти, это все ориентировочно и ты можешь справиться со своей целью быстрей!')
a = int(input('Введи сколько километров ты сегодня пробежал: '))
b = int(input('Какая твоя цель: '))
improvement: int = 10 / 100 * a
results: int = ((b - a) // improvement) + 1
print(f'Ты пробежишь {b} километров спустя {results} дней, если продолжишь в том же ритме улучшать результат ежедневно')