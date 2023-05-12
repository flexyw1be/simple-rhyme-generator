import requests
from random import choice
from nltk.stem.snowball import RussianStemmer

stemmer = RussianStemmer()

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/86.0.4240.185 YaBrowser/20.11.2.78 Yowser/2.5 Safari/537.36', 'accept': '*/*'}


def prepare_prompt(s):
    s = ''.join([i for i in s.lower().split()[-1] if i in 'йцукенгшщзхъэждлорпавыфячсмитьбю'])
    return s


def get_rhyme(x):
    x = prepare_prompt(x)
    url = f'https://rifmovka.ru/rifma/{x}'
    r = requests.get(url, headers=HEADERS)
    try:
        s = r.text.replace('<b>', '').replace('</b>', '')
        s = s[s.index('meta name="description"'):s.index('<meta name="keywords"')].replace('...">', '').strip()
        ln = len(f'Рифма к слову {x}:  ')
        s = s[s.index('Рифма к слову ') + ln:].split(', ')
    except Exception:
        s = [x]

    return choice(s)


