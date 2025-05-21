from collections import defaultdict
import re
import time

class TextSearcher:
    def __init__(self, file_path):
        self.word_count = defaultdict(int)
        self.index = defaultdict(list)
        self.total_words = 0

        start_time = time.time()
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        words = re.findall(r'\b\w+\b', text)
        self.total_words = len(words)

        for word in words:
            self.word_count[word] += 1

        for word in self.word_count:
            substrings = set()
            for i in range(len(word) - 2):
                for j in range(i + 3, len(word) + 1):
                    substrings.add(word[i:j])
            for substr in substrings:
                self.index[substr].append(word)

        for substr in self.index:
            self.index[substr].sort(key=lambda w: -self.word_count[w])

        print(f"Инициализация заняла {time.time() - start_time:.2f} сек.")

    def search(self, query):
        if len(query) < 3:
            return []

        query = query.lower()
        matching_words = self.index.get(query, [])
        return matching_words[:20]

if __name__ == "__main__":
    print("\nАвтор: Колесников Сергей Николаевич")
    print("Группа: 020303-АИСа-о24")
    searcher = TextSearcher("war_and_peace.txt")

    while True:
        query = input("Введите запрос (>=3 символов): ").strip()
        if not query:
            break

        start_time = time.time()
        results = searcher.search(query)
        elapsed = time.time() - start_time

        print(f"Найдено {len(results)} слов (за {elapsed:.4f} сек):")
        for i, word in enumerate(results, 1):
            print(f"{i}. {word} (встречается {searcher.word_count[word]} раз)")