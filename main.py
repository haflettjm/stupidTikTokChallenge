
#stupid stupid tik tok math challenge https://youtube.com/shorts/snlJdE4A0c4?feature=share


#main logic
def main():

    #annoying tik tok challenge
    numbers = [1,3,5,7,9,11,13,15]
    answerable = False
    ansNums = []

    for x in range(len(numbers)):
        for y in range(len(numbers)):
            for z in range(len(numbers)):
                if x+y+z == 30:
                    answerable = True
                    ansNums.append([z,y,x])

    if answerable == True:
        print(f'The challenge has an answer of:', ansNums)
    else:
        print("There is no answer")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()