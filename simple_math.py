import random

print (">>>>> WELCOME TO <<<<")
print (">>>>> MATH GAME <<<<<")
print (">>>>>>>>>>><<<<<<<<<<")

operation = ["+", "-", "/", "*"]

def game(a, b, c):
  match c:
    case "+": return a + b
    case "-": return a - b
    case "/": return a / b
    case "*": return a * b


while True:
    f_n = random.randint(1, 10)
    s_n = random.randint(1, 10)
    o_r = random.choice(operation)
    # f_n (first number)
    # s_n (second number)
    # o_r (operation random)
    result = (game(f_n, s_n, o_r))
    print(f"--› {f_n} {o_r} {s_n} = ?")
    try:
      u_i = float(input("--› "))
      # u_i (user input)
    except ValueError:
      print ("----› Please,enter a valid number!!!")
      
    if o_r == "/" and abs(u_i - result) < 0.01:
      print(f"--› Correct!!!, good job!!! The answer is {result}")
    elif u_i == result:
      print(f"--› Correct!!!, good job!!! The answer is {result}")
    else:
      print(f"--› Oops, that's not correct!!!, the answer is {result}")
      
    again = input("--› Wanna play again? (y / n)? : ").lower()
    if again != "y":
      print("--› Thanks for playing this game!!!!, Bye...")
      break
      
    
  