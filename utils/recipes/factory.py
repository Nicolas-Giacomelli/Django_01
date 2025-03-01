<<<<<<< HEAD
#Definindo função de testes, ira preencher com palavras 'fake'
#apenas para rodar os testes e verificar existencia de erros


#from inspect import signature

=======
# from inspect import signature
>>>>>>> c976c6b (Aula_62)
from random import randint

from faker import Faker

<<<<<<< HEAD
def rand_ratio():
    return randint(840,900 ), randint(473,573)

fake = Faker('pt_BR')
#print(signature(fake.random_number))
=======

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))

>>>>>>> c976c6b (Aula_62)

def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
<<<<<<< HEAD
        'title':fake.sentence(nb_words=6),
        'description':fake.sentence(nb_words=12),
=======
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
>>>>>>> c976c6b (Aula_62)
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
<<<<<<< HEAD
        'preparation_steps':  fake.text(3000),
=======
        'preparation_steps': fake.text(3000),
>>>>>>> c976c6b (Aula_62)
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
<<<<<<< HEAD
            'name': fake.word(),   
=======
            'id':fake.random_number(digits=2, fix_len=True),
            'name': fake.word()
>>>>>>> c976c6b (Aula_62)
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

<<<<<<< HEAD
if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
=======

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
>>>>>>> c976c6b (Aula_62)
