class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.parent = None
        self.next = None  # Powiązana lista liści (dla zapytań zakresowych)

class BPlusTree:
    def __init__(self, order=4):
        self.root = BPlusTreeNode(is_leaf=True)
        self.order = order
        self.comparisons = 0

    def find_leaf(self, key):
        current = self.root
        while not current.is_leaf:
            for i, k in enumerate(current.keys):
                self.comparisons += 1
                if key < k:
                    current = current.children[i]
                    break
            else:
                current = current.children[-1]
        return current

    def add_player(self, key, player_name):
        leaf = self.find_leaf(key)
        self.comparisons += len(leaf.keys)
        for i, k in enumerate(leaf.keys):
            if key == k:
                leaf.children[i].append(player_name)
                return
            elif key < k:
                leaf.keys.insert(i, key)
                leaf.children.insert(i, [player_name])
                break
        else:
            leaf.keys.append(key)
            leaf.children.append([player_name])
        if len(leaf.keys) >= self.order:
            self.split_node(leaf)

    def split_node(self, node):
        mid = len(node.keys) // 2
        new_node = BPlusTreeNode(is_leaf=node.is_leaf)
        new_node.keys = node.keys[mid:]
        new_node.children = node.children[mid:]
        node.keys = node.keys[:mid]
        node.children = node.children[:mid]
        new_node.parent = node.parent
        if node.is_leaf:
            new_node.next = node.next
            node.next = new_node

        if node == self.root:
            new_root = BPlusTreeNode()
            new_root.keys = [new_node.keys[0]]
            new_root.children = [node, new_node]
            self.root = new_root
            node.parent = self.root
            new_node.parent = self.root
        else:
            parent = node.parent
            new_key = new_node.keys[0]
            for i, k in enumerate(parent.keys):
                self.comparisons += 1
                if new_key < k:
                    parent.keys.insert(i, new_key)
                    parent.children.insert(i + 1, new_node)
                    break
            else:
                parent.keys.append(new_key)
                parent.children.append(new_node)
            if len(parent.keys) >= self.order:
                self.split_node(parent)

    def update_player(self, old_key, new_key, player_name):
        self.delete_player(old_key, player_name)
        self.add_player(new_key, player_name)

    def delete_player(self, key, player_name):
        leaf = self.find_leaf(key)
        self.comparisons += len(leaf.keys)
        for i, k in enumerate(leaf.keys):
            if key == k:
                if player_name in leaf.children[i]:
                    leaf.children[i].remove(player_name)
                    if not leaf.children[i]:
                        leaf.keys.pop(i)
                        leaf.children.pop(i)
                return

    def find_range(self, min_key, max_key):
        leaf = self.find_leaf(min_key)
        result = []
        while leaf:
            for i, key in enumerate(leaf.keys):
                self.comparisons += 1
                if min_key <= key <= max_key:
                    result.extend(leaf.children[i])
                elif key > max_key:
                    return result
            leaf = leaf.next
        return result

    def find_best_player(self):
        leaf = self.root
        while not leaf.is_leaf:
            leaf = leaf.children[-1]
        return leaf.children[-1]

    def find_worst_player(self):
        leaf = self.root
        while not leaf.is_leaf:
            leaf = leaf.children[0]
        return leaf.children[0]

    def get_player_score(self, player_name):
        leaf = self.root
        while leaf:
            for i, players in enumerate(leaf.children):
                self.comparisons += len(players)
                if player_name in players:
                    return leaf.keys[i]
            leaf = leaf.next
        return None

def test_bplus_tree():
    # Tworzenie drzewa B+ z rozmiarem rzędu 4
    tree = BPlusTree(order=4)

    # Test: Dodawanie graczy
    print("\nDodawanie graczy:")
    tree.add_player(100, "PlayerA")
    tree.add_player(200, "PlayerB")
    tree.add_player(150, "PlayerC")
    tree.add_player(100, "PlayerD")  # Wynik 100, ten sam wynik co PlayerA
    print(f"Liczba porównań: {tree.comparisons}")
    
    # Test: Sprawdzanie najlepszego gracza
    print("\nNajlepszy gracz:")
    best_player = tree.find_best_player()
    print(f"Najlepszy gracz: {best_player}")
    print(f"Liczba porównań: {tree.comparisons}")

    # Test: Sprawdzanie najgorszego gracza
    print("\nNajgorszy gracz:")
    worst_player = tree.find_worst_player()
    print(f"Najgorszy gracz: {worst_player}")
    print(f"Liczba porównań: {tree.comparisons}")

    # Test: Sprawdzanie wyniku konkretnego gracza
    print("\nSprawdzanie wyniku gracza:")
    score = tree.get_player_score("PlayerC")
    print(f"Wynik PlayerC: {score}")
    print(f"Liczba porównań: {tree.comparisons}")

    # Test: Aktualizacja wyniku gracza
    print("\nAktualizacja wyniku gracza:")
    tree.update_player(150, 250, "PlayerC")  # Aktualizacja wyniku PlayerC na 250
    score = tree.get_player_score("PlayerC")
    print(f"Zaktualizowany wynik PlayerC: {score}")
    print(f"Liczba porównań: {tree.comparisons}")

    # Test: Zapytanie o zakres punktów
    print("\nZapytanie o zakres punktów (100-200):")
    players_in_range = tree.find_range(100, 200)
    print(f"Gracze w zakresie 100-200 punktów: {players_in_range}")
    print(f"Liczba porównań: {tree.comparisons}")

    # Test: Usuwanie gracza
    print("\nUsuwanie gracza:")
    tree.delete_player(200, "PlayerB")
    print(f"Liczba porównań: {tree.comparisons}")
    score = tree.get_player_score("PlayerB")
    print(f"Sprawdzanie wyniku PlayerB po usunięciu: {score}")

# Uruchomienie testów
test_bplus_tree()
