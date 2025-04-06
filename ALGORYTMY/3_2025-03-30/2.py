words_array = [
    "kwiat", "słońce", "księżyc", "gwiazda", "rzeka", "góra", "las", "morze", "niebo", "chmura", "ptak", "pies", "kot", "ryba", "drzewo", "ziemia", "ogień", "woda", "kamień", "piasek", "liść", "płomień", "wiatr", "deszcz", "śnieg", "mróz", "wiosna", "lato", "jesień", "zima", "człowiek", "serce", "dusza", "myśl", "uczucie", "dom", "miasto", "wieś", "most", "droga", "auto", "rower", "pociąg", "samolot", "statek", "zegar", "czas", "minuta", "godzina", "dzień", "noc", "tydzień", "miesiąc", "rok", "książka", "obraz", "pióro", "papier", "list", "długopis", "komputer", "telefon", "okno", "drzwi", "stół", "krzesło", "łóżko", "szafa", "lustro", "ściana", "podłoga", "dach", "ogród", "kwiaty", "trawa", "jabłko", "gruszka", "wiśnia", "truskawka", "malina", "winogrono", "pomidor", "ogórek", "marchewka", "burak", "cebula", "czosnek", "sól", "cukier", "chleb", "masło", "mleko", "ser", "mięso", "ryż", "makaron", "wino", "piwo", "mąka", "kapusta"
]

#a -> C: O(n) / P: O(n)
def search_array(prefix, words):
    step_count = 0
    result = []
    for word in words:
        step_count += 1
        if word.startswith(prefix):
            result.append(word)
    return result, step_count

prefix = "mi"
result, step_count = search_array(prefix, words_array)
print("\n#a:")
print(f"Słowa: {result}")
print(f"Liczba słów: {len(result)}")
print(f"Liczba kroków: {step_count}")

#b -> C: O(n) / P O([liczba liter w alfabecie] * [łączna długość wszystkich słów w strukturze])

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def collect_words(self, node, prefix=""):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char, child in node.children.items():
            result += self.collect_words(child, prefix + char)
        return result

    def search_prefix(self, prefix):
        node = self.root
        step_count = 0
        for char in prefix:
            step_count += 1
            if char not in node.children:
                return [], step_count
            node = node.children[char]
        return self.collect_words(node), step_count

trie = Trie()
for word in words_array:
    trie.add_word(word)

prefix = "mi"
result, step_count = trie.search_prefix(prefix)
print("\n#b:")
print(f"Słowa: {result}")
print(f"Liczba słów: {len(result)}")
print(f"Liczba kroków: {step_count}")