import random

def play_ace_of_cards_game():
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    random.shuffle(deck)
    
    player1_hand = []
    player2_hand = []
    
    for _ in range(5):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())
    
    player1_score = sum_card_values(player1_hand)
    player2_score = sum_card_values(player2_hand)
    
    print("Welcome to the Ace of Cards Game!")
    print("\nPlayer 1's Hand:", player1_hand)
    print("Player 1's Score:", player1_score)
    print("\nPlayer 2's Hand:", player2_hand)
    print("Player 2's Score:", player2_score)
    
    winner = determine_winner(player1_score, player2_score)
    print("\n" + winner)
    
def sum_card_values(hand):
    values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    total = 0
    
    for card in hand:
        total += values[card]
    
    return total

def determine_winner(score1, score2):
    if score1 > score2:
        return "Player 1 wins!"
    elif score1 < score2:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

play_ace_of_cards_game()




#1 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Create a rectangle object with length 5 and width 3
rect = Rectangle(5, 3)

# Calculate and print the area
area = rect.calculate_area()
print("Area of the rectangle:", area)




#2 
class Student:
    def __init__(self, name, id, dept, grad):
        self.name = name
        self.id = id
        self.dept = dept
        self.grad = grad

    def calculate_average(self):
        # Assuming you have grades for the student, calculate the average here
        grades = [85, 92, 78]  # Example grades
        return sum(grades) / len(grades)

    def print_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.dept)
        print("Graduation Year:", self.grad)
        print("Average Grade:", self.calculate_average())

# Create a student object
student = Student("Alice", 12345, "Computer Science", 2024)

# Print the student's information
student.print_info()