#guess the number
n=78
p=1
while(p<=5):
    print("enter the number\n")
    inp = int(input())
    if (inp<78):
        print("number is bigger than the number u have written")

    elif (inp>78):
        print("number is smaller than the number u have written")
    else:
        print("you won")
        break
    print(5-p,"no. of guesses left")
    p=p+1

if (p>6):
    print("u reach the limit")

