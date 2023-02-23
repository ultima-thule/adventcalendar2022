f = open("day2_input.txt", "r")

#A - kamień, B - papier, C - nożyce
#X - kamień, Y - papier, Z - nożyce
winners = {"A X": 3+1, "B X": 0+1, "C X": 6+1,
           "A Y": 6+2, "B Y": 3+2, "C Y": 0+2,
           "A Z": 0+3, "B Z": 6+3, "C Z": 3+3}

result = 0

#A - kamień, B - papier, C - nożyce
#X1 - lose, Y - draw, Z - win
#X2 - kamień, Y - papier, Z - nożyce
response = {"A X": "A Z", "B X": "B X", "C X": "C Y",
            "A Y": "A X", "B Y": "B Y", "C Y": "C Z",
            "A Z": "A Y", "B Z": "B Z", "C Z": "C X"}


for line in f:
    line = line.strip()
    #print(f"linijka: {line}, przetlumaczone: {translated}", line, translated)
    result += winners[response[line]]


print(result)

f.close()
