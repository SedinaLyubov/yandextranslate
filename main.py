import requests

def translate_word(word):
    url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
    token = 'dict.1.1.20231029T152749Z.de2a2c03ec748f84.c058f99060396b8496f591c5b045ed578338dfc3'
    param = {
            'key': token,
            'lang': 'ru-en',
            'text': word
    }
    resp = requests.get(url=url, params=param).json()
    trans_word = resp['def'][0]['tr'][0]['text']
    print(trans_word)
translate_word('собака')
#if __name__ == '__main__':
#    word = 'машина'
#    assert translate_word(word) == 'car'