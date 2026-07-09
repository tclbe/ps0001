#%% Easy Q1
print("hello", "world")
print("hello world")

#%% Easy Q2
print(123 * 987)
print(987 * 123)

#%% Easy Q3
alice = 839
bob = 1098
eve = 373
print("They have", (alice + bob + eve) / 3, "dollars on average between them.")

#%%
print("They have", (839 + 1098 + 373) / 3, "dollars on average between them.")

#%% Easy Q4
my_name = "Caleb"
my_age = 26
print("my name is", my_name, "and i am", my_age, "years old.")
hours = my_age * 365 * 24
print(my_age, "years is", hours, "hours")

#%% Medium Q1
moneyInWallet = 24
priceOfChickenRice = 4
priceOfCoffee = 2
moneyInWallet = moneyInWallet - priceOfChickenRice - priceOfCoffee
print("I have", moneyInWallet, "dollars after my lunch.")

#%% Medium Q2
first = 12
second = first - 5
first = first * second
second = second - 5
first = second * 5

#%% Medium Q3
a = 5
b = 7
t = b
b = a
a = t

#%% Medium Q3
a = 5
b = 7
a, b = b, a

#%% Hard Q1
original_hours = 12345
days = int(original_hours / 24)
print(original_hours, "hours is about", days, "days.")
years = int(days / 365)
days = days - years * 365
hours = original_hours - years * 365 * 24 - days * 24
print("There are", years, "year(s),", days, "day(s), and", hours, "hour(s) in",
      original_hours, "hours.")
