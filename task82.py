'''Task 8.2'''
with open('stdin.txt', 'r', encoding = 'UTF-8') as inputFile:
    with open('stdout.txt', 'w', encoding = 'UTF-8') as outputFile:
        userNumbers = inputFile.readline()
        ANSWER = 0
        for number in userNumbers:
            ANSWER += int(number)
        outputFile.writelines([str(ANSWER)])
