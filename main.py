import random
import time
import os

class UserManager:
    def __init__(self):
        self.users = []
        os.system('cls')
        print("******Welcome********")
        time.sleep(1)
        os.system('cls')

    def add_user(self):
        print("-"*30)
        try:
            add = input("Enter the name of the user to be added: ")
            self.users.append(add)
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_users(self):
        print("-"*30)
        try:
            count = 1
            for user in self.users:
                print(str(count) + "-Username: ", user)
                count += 1
            print("-"*30)
        except Exception as e:
            print(f"An error occurred: {e}")

    def select_user(self):
        while True:
            print("-"*30)
            try:
                select_user = int(input("How many people will be selected? "))
                if select_user > len(self.users):
                    print("Error! Number of selections exceeds the number of available users.")
                    continue  # Prompt the user to re-enter a valid number
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
        
        try:
            random_select = random.sample(self.users, select_user)
            print("Loading...")
            time.sleep(2)

            count = 1
            for user in random_select:
                print(str(count) + "-Username: ", user)
                count += 1
            print("-"*30)
            input("Press Enter to continue...")
        except Exception as e:
            print(f"An error occurred: {e}")

    def mix_users(self):
        print("-"*30)
        try:
            count = 1
            random.shuffle(self.users)
            for user in self.users:
                print(str(count) + "-Username: ", user)
                count += 1
            print("-"*30)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    manager = UserManager()
    while True:
        try:
            choose = int(input("1-Add User\n2-Show User\n3-Select User\n4-Mix User\n"))
            if choose == 1:
                manager.add_user()
            elif choose == 2:
                manager.show_users()
            elif choose == 3:
                manager.select_user()
            elif choose == 4:
                manager.mix_users()
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
