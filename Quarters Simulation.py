import matplotlib.pyplot as plt
import numpy as np

totalOptions = int(input("Type number of options you want "))
totalTests = int(input("Type number of tests you want "))
Options = np.arange(0, totalOptions)
Occurrences = np.array([0 for i in range(len(Options))])

quarterThrows = 0

lenOfOptions = len(Options)
while lenOfOptions != 0:
    lenOfOptions = lenOfOptions // 2
    quarterThrows += 1
while True:
    try:
        trulyRandom = True if input("Type 0 for trulyRandom, 1 for faster method ") == "0" else False
        break
    except ValueError:
        print("Enter a boolean True or False ")

quarterThrownAmount = 0

def quartersThrown(num_times = 5):
    def quarterThrownCounter(func):
        def wrapper(*args, **kwargs):
            global quarterThrownAmount
            quarterThrownAmount += num_times
            return func(*args, **kwargs)

        return wrapper
    return quarterThrownCounter
@quartersThrown(quarterThrows)
def deterimineBinaryNumberObtainedFromCoinTosses(quarterThrows: int = 5) -> str:
    binary = ""
    for number in range(quarterThrows):
        if np.random.randint(0, 2) == 0:
            binary += "0"
        else:
            binary += "1"
    return binary


def convertBinaryToDecimal(binary: str) -> int:
    value = 0
    binary = binary[::-1]
    for place, letter in enumerate(binary):
        value += (2 ** place) * int(letter)
    return value







for number in range(totalTests):
    if trulyRandom:
        val = deterimineBinaryNumberObtainedFromCoinTosses(quarterThrows)
        while convertBinaryToDecimal(val) >= len(Options):
            val = deterimineBinaryNumberObtainedFromCoinTosses(quarterThrows)
        Occurrences[convertBinaryToDecimal(val)] += 1
    else:
        val = deterimineBinaryNumberObtainedFromCoinTosses(quarterThrows)
        while convertBinaryToDecimal(val) % 2 ** quarterThrows >= len(Options):
            quarterThrownAmount += 1
            if np.random.randint(0, 2) == 0:
                val += "0"
            else:
                val += "1"
        else:
            Occurrences[convertBinaryToDecimal(val) % 2 ** quarterThrows] += 1

# Creating the bar graph
plt.bar(Options, Occurrences)

# Adding titles and labels
plt.title('Option Chosen by Quarter')
plt.xlabel('Option Number')
plt.ylabel('Occurrences of Option')

# Show the plot
plt.show()

# Show the number of times the quarter had to be thrown
print(f'The quarter was thrown {quarterThrownAmount} times to receive this result')
