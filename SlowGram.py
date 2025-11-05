from UDGraph import UDGraph
from Person import Person

class SlowGram:
    def __init__(self):
        self.graph = UDGraph()
        self.people = []

    # Create user profiles and relationships
    def setup_data(self):
        p1 = Person("Jonathan", "P", "Traveler and photographer.")
        p2 = Person("Jay Teh", "U", "Tech enthusiast and gamer.")
        p3 = Person("Han Yi", "P", "Food blogger and coffee lover.")
        p4 = Person("Dhevagar", "P", "Fitness trainer and motivator.")
        p5 = Person("Koed Zu", "U", "Digital artist and dreamer.")

        self.people = [p1, p2, p3, p4, p5]

        for p in self.people:
            self.graph.add_vertex(p)

        # Follow relationships (directed)
        self.graph.add_edge(p1, p3)  # Alicia -> Nora
        self.graph.add_edge(p1, p4)  # Alicia -> Jason
        self.graph.add_edge(p2, p1)  # David -> Alicia
        self.graph.add_edge(p3, p4)  # Nora -> Jason
        self.graph.add_edge(p4, p5)  # Jason -> Sarah
        self.graph.add_edge(p5, p1)  # Sarah -> Alicia

    # (a) Display all users
    def view_all_profiles(self):
        print("\n-----------------------------------------")
        print(" List of All Registered Users")
        print("-----------------------------------------")
        for i, person in enumerate(self.people, start=1):
            print(f"{i}. {person.get_name()}")

    # (b) View profile (ignoring privacy)
    def display_profile(self, index):
        people = self.people
        if 0 <= index - 1 < len(people):
            person = people[index - 1]
            print("\n-----------------------------------------")
            print(" Profile Information")
            print("-----------------------------------------")
            print(f"Name     : {person.get_name()}")
            print(f"Privacy  : {'Public' if person.get_privacy() == 'P' else 'Private'}")
            print(f"Biography: {person.get_biography()}")
            print("-----------------------------------------")
        else:
            print("Invalid profile number.")

    # (c) View followed accounts (outgoing edges)
    def view_following(self, index):
        people = self.people
        if 0 <= index - 1 < len(people):
            person = people[index - 1]
            print("\n-----------------------------------------")
            print(f" Accounts followed by {person.get_name()}:")
            print("-----------------------------------------")
            following = self.graph.list_outgoing_adjacent_vertex(person)
            if following:
                for f in following:
                    print(f"- {f.get_name()}")
            else:
                print("No followed accounts.")
            print("-----------------------------------------")
        else:
            print("Invalid profile number.")

    # (d) View followers (incoming edges)
    def view_followers(self, index):
        people = self.people
        if 0 <= index - 1 < len(people):
            selected = people[index - 1]
            print("\n-----------------------------------------")
            print(f" Followers of {selected.get_name()}:")
            print("-----------------------------------------")
            followers = []
            for user, follows in self.graph.graph.items():
                if selected in follows:
                    followers.append(user.get_name())
            if followers:
                for f in followers:
                    print(f"- {f}")
            else:
                print("No followers found.")
            print("-----------------------------------------")
        else:
            print("Invalid profile number.")

    # Menu
    def menu(self):
        print("\n=========================================")
        print("  Welcome to SlowGram Social Media App ")
        print("=========================================")
        print("1.  View all user names")
        print("2.  View profile details (ignore privacy)")
        print("3.  View followed accounts")
        print("4. ️  View followers")
        print("5.  Quit")
        print("=========================================")

    # Run program
    def run(self):
        self.setup_data()
        choice = ""
        while choice != "5":
            self.menu()
            choice = input("Enter your choice (1 - 5): ")

            if choice == "1":
                self.view_all_profiles()

            elif choice == "2":
                self.view_all_profiles()
                index = int(input("\nSelect profile number to view details (1 - 5): "))
                self.display_profile(index)

            elif choice == "3":
                self.view_all_profiles()
                index = int(input("\nSelect profile number to view followed accounts (1 - 5): "))
                self.view_following(index)

            elif choice == "4":
                self.view_all_profiles()
                index = int(input("\nSelect profile number to view followers (1 - 5): "))
                self.view_followers(index)

            elif choice == "5":
                print("\nThank you for using SlowGram! Goodbye ")
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = SlowGram()
    app.run()
