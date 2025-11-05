import time

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id} - {self.name}"

class HashTableLinked:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = self.Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = self.Node(key, value)

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

def main():
    products = [
        Product("P001", "Baby Milk", "Food", 25.5, 50),
        Product("P002", "Baby Diapers", "Hygiene", 45.0, 80),
        Product("P003", "Baby Lotion", "Skincare", 18.9, 40),
        Product("P004", "Baby Bottle", "Feeding", 12.5, 60),
        Product("P005", "Baby Wipes", "Hygiene", 10.0, 100)
    ]

    # Insert into both structures
    hash_table = HashTableLinked(10)
    for p in products:
        hash_table.insert(p.product_id, p)
    product_array = products.copy()

    # Measure hash table search time
    start_hash = time.perf_counter()
    result_hash = hash_table.search("P002")
    end_hash = time.perf_counter()

    # Measure array search time
    start_arr = time.perf_counter()
    result_arr = None
    for p in product_array:
        if p.product_id == "P002":
            result_arr = p
            break
    end_arr = time.perf_counter()

    # Calculate times in milliseconds
    hash_ms = (end_hash - start_hash) * 1000
    arr_ms = (end_arr - start_arr) * 1000

    # Display results
    print("Hash Table Search Result:", result_hash)
    print("Array Search Result:", result_arr)
    print("\nHash Table Search Time: {:.6f} ms".format(hash_ms))
    print("Array Search Time: {:.6f} ms".format(arr_ms))

if __name__ == "__main__":
    main()
