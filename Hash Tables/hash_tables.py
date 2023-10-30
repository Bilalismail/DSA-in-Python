class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            # Handle collision with chaining
            current = self.table[index]
            while current.next and current.key != key:
                current = current.next
            if current.key == key:
                # If key is already present, update the value
                current.value = value
            else:
                # Append new key-value pair to the list
                current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current and current.key != key:
            current = current.next
        if current:
            return current.value
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current and current.key != key:
            prev = current
            current = current.next
        if not current:
            return None  # Key not found
        if prev:
            prev.next = current.next
        else:
            self.table[index] = current.next

    def __str__(self):
        result = []
        for head in self.table:
            while head:
                result.append(f"{head.key} => {head.value}")
                head = head.next
        return ";\n".join(result)
h = Hashtable()
h.set("name", "John")
h.set("age", "25")
h.set("country", "US")

print(h.get("name"))     # Outputs: John
print(h.get("country"))  # Outputs: US
print(h)

h.delete("age")
print(h)
