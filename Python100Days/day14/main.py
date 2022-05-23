# Import art logo
import art
print(art.logo)

from game_data import data
def get_competitor(data):
  import random
  return data[random.randint(0, len(data) - 1)]

def get_initial_competitors():
  competitors = []
  competitors.append(get_competitor(data))
  competitors.append(get_competitor(data))
  return competitors

# Display Object A # Display VS symbol logo # Display Object B
def show_match_info(competitors):
  competitor_a = competitors[0]
  competitor_b = competitors[1]
  print(f"Compare A: {competitor_a['name']}, a {competitor_a['description']}, from {competitor_a['country']}")
  print(art.vs)
  print(f"Compare B: {competitor_b['name']}, a {competitor_b['description']}, from {competitor_b['country']}")

def calculate_score(competitors, choice, score):
  follower_count_a = competitors[0]['follower_count']
  follower_count_b = competitors[1]['follower_count']
  user_choice, cpu_choice = 0, 0
  
  if choice == "A":
    user_choice = follower_count_a
    cpu_choice = follower_count_b
  else:
    user_choice = follower_count_b
    cpu_choice = follower_count_a
  
  if user_choice > cpu_choice:
    return score + 1
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    return 0

def next_match(competitors):
  new_competitors = []
  new_competitors.append(competitors.pop())
  new_competitors.append(get_competitor(data))
  return new_competitors
  

def game():
  score = 0
  competitors = get_initial_competitors()
  show_match_info(competitors)
  # Ask user input who has more followers? Type 'A' or 'B'
  choice = input("Who has more followers? Type 'A' or 'B': ")
  score = calculate_score(competitors, choice, score)

  while score != 0:
    print(f"\nYou're right! Current score: {score}")
    new_competitors = next_match(competitors)
    show_match_info(new_competitors)
    choice = input("Who has more followers? Type 'A' or 'B': ")
    score = calculate_score(new_competitors, choice, score)
    competitors = new_competitors
    if score == 0:
      return

game()
  




