#inventory_system

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id:<6} | {self.name:<15} | {self.category:<10} | RM{self.price:<8.2f} | {self.quantity:<5}"


class HashTableLinked:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = self.Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            new_node = self.Node(key, value)
            current.next = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def get_all_products(self):
        all_items = []
        for bucket in self.table:
            current = bucket
            while current:
                all_items.append(current.value)
                current = current.next
        return all_items


def create_sample_data(inventory):
    inventory.insert("P001", Product("P001", "Baby Milk", "Food", 25.5, 50))
    inventory.insert("P002", Product("P002", "Baby Diapers", "Hygiene", 45.0, 80))
    inventory.insert("P003", Product("P003", "Baby Lotion", "Skincare", 18.9, 40))
    inventory.insert("P004", Product("P004", "Baby Bottle", "Feeding", 12.5, 60))
    inventory.insert("P005", Product("P005", "Baby Wipes", "Hygiene", 10.0, 100))


def show_menu():
    print("\n" + "=" * 45)
    print("      BABY SHOP INVENTORY MANAGEMENT SYSTEM      ")
    print("=" * 45)
    print("1. Add New Product")
    print("2. Search Product")
    print("3. Edit Product")
    print("4. Delete Product")
    print("5. View All Products")
    print("6. Exit")
    print("=" * 45)


def show_table(products):
    print("\n{:<6} | {:<15} | {:<10} | {:<10} | {:<5}".format(
        "ID", "Name", "Category", "Price", "Qty"))
    print("-" * 55)
    for p in products:
        print(p)
    print("-" * 55)


def main():
    inventory = HashTableLinked(10)
    create_sample_data(inventory)

    choice = ""
    while choice != "6":
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            cat = input("Enter Category: ").strip()
            try:
                price = float(input("Enter Price: "))
                qty = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            inventory.insert(pid, Product(pid, name, cat, price, qty))
            print("✅ Product added successfully!")

        elif choice == "2":
            pid = input("Enter Product ID to search: ").strip()
            product = inventory.search(pid)
            if product:
                print("\nProduct found:")
                print("-" * 55)
                print("ID     | Name            | Category  | Price     | Qty")
                print("-" * 55)
                print(product)
                print("-" * 55)
            else:
                print("❌ Product not found!")

        elif choice == "3":
            pid = input("Enter Product ID to edit: ").strip()
            product = inventory.search(pid)
            if product:
                print("\nCurrent Product Details:")
                print(product)
                try:
                    new_price = float(input("Enter new Price: "))
                    new_qty = int(input("Enter new Quantity: "))
                except ValueError:
                    print("Invalid input.")
                    continue
                product.price = new_price
                product.quantity = new_qty
                print("✅ Product updated successfully!")
            else:
                print("❌ Product not found!")

        elif choice == "4":
            pid = input("Enter Product ID to delete: ").strip()
            deleted = inventory.delete(pid)
            if deleted:
                print("🗑️ Product deleted successfully!")
            else:
                print("❌ Product not found!")

        elif choice == "5":
            all_products = inventory.get_all_products()
            if all_products:
                print("\n📦 Current Inventory List:")
                show_table(all_products)
            else:
                print("No products available.")

        elif choice == "6":
            print("👋 Exiting system... Goodbye!")

        else:
            print("Invalid choice. Please enter 1–6.")


# Driver
if __name__ == "__main__":
    main()
