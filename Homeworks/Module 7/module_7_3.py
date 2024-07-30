class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8')as f:
                text = f.read().lower()
                for punct_marks in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct_marks, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_positions = {}
        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1
            else:
                word_positions[file_name] = None
        return word_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_count = {}
        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word)
        return word_count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('captain'))     # Позиция слова 'TEXT'
print(finder2.count('captain'))    # Количество слова 'teXT'
