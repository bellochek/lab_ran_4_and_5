from collections import defaultdict, Counter
import time


class DictionarySolver:
    def __init__(self, dictionary_file):
        self.word_list = []
        self.length_to_words = defaultdict(list)
        self.word_to_counter = {}

        with open(dictionary_file, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()

        for word in words:
            word = word.strip().lower()
            if not word:
                continue
            counter = Counter(word)
            self.word_to_counter[word] = counter
            length = len(word)
            self.length_to_words[length].append(word)
            self.word_list.append(word)

        self.sorted_lengths = sorted(self.length_to_words.keys(), reverse=True)

    def find_words(self, input_word):
        input_counter = Counter(input_word.lower())
        result = []

        for length in self.sorted_lengths:
            for word in self.length_to_words[length]:
                word_counter = self.word_to_counter[word]
                # Проверяем, что все буквы слова есть в input_word в достаточном количестве
                valid = True
                for char, count in word_counter.items():
                    if input_counter[char] < count:
                        valid = False
                        break
                if valid:
                    result.append(word)

        return result

if __name__ == "__main__":
    print("\nАвтор: Колесников Сергей Николаевич")
    print("Группа: 020303-АИСа-о24")
    start_time = time.time()
    solver = DictionarySolver("russian_nouns.txt")
    print(f"Инициализация заняла {time.time() - start_time:.2f} сек.")

    input_word = "абстракция"
    start_time = time.time()
    result = solver.find_words(input_word)
    print(f"Поиск слов занял {time.time() - start_time:.2f} сек.")

    print(f"Слова, которые можно составить из '{input_word}':")
    for word in result:
        print(word)