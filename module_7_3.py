# Задача "Найдёт везде"

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        str_punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as megafile:
                words_txt = []
                for line in megafile:
                    lines = line.lower()
                    for p in str_punct:
                        lines = lines.replace(p, ' ')
                    words_txt += lines.split()
                all_words[name] = words_txt
        return all_words

    def find(self, word):
        for i in self.get_all_words().items():
            find_word = word.lower()
            if find_word in i[1]:
                return {i[0]: (i[1].index(find_word) + 1)}

    def count(self, word):
        count_words = 0
        for i in self.get_all_words().items():
            list_words = i[1]
            if word.lower() in list_words:
                for j in range(len(list_words)):
                    if list_words[j] == word.lower():
                        count_words += 1
                return {i[0]: count_words}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
