from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    jokes = []
    while len(jokes) < n:
        word1, word2, word3 = choice(nouns), choice(adverbs), choice(adjectives)
        joke = f'{word1} {word2} {word3}'
        jokes.append(joke)
    return jokes


print(get_jokes(8))
