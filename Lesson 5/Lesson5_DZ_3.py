from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена',"Жанна", "Валентина", "Елизавета"]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '10А', "5А", "7Б"]

generator=((tutor,klass) for tutor, klass in zip_longest(tutors,klasses))
for i in generator:
    print(i)


