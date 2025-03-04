def fizz_buzz(input):  #input is i
    if (input%3==0) and (input%5==0):
        return "FizzBuzz"
    elif input%5==0:
        return "buzz"
    elif input%3 ==0:
        return "fizz"
    else :
        return input

print(fizz_buzz(15))  #if the input tht we give is divisible by 3 its return the  string fizz  and if the input is divisible by 5 if returns buzz and if the input is divible by both it will give fizzbuzz and for any aother nos it will return that no its self