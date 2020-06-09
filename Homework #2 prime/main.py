#Tell if number is prime
def checkPrime(num):
    if num > 1:
        #check all numbers from 2 to number to see if it divides with no remainded
        for i in range(2, num):
            if num%i is 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

    sieve(num)

# to find all prime numbers smaller than the num givem, the sieve of Eratosthenes will be used
def sieve(num):
    #fill list with values not including 0
    prime = list(range(1,num+1))
    #as values get removed, they will not be looped through as they are deleted
    for num in prime:
        #not 1
        if num is not 1:
            #check all remianing numbers and exclude self. using != instead of is not
            #since we are checking values. is not would always fail
            for check in prime:
                if check != num:
                    if check%num == 0:
                        prime.remove(check)
    #write all numbers left in list to file. with open closes file when out of scope
    with open('EvanJacksonH2.txt', 'w') as primeWrite:
        for num in prime:
            primeWrite.write(f"{num}\n")


def printPrimes(path):
    with open(path, 'r') as fp:
        lines = fp.readlines()
        #remove '\n' from lines list values
        for prime in lines:
            print(prime.strip('\n'), end='\t')


def main():
    num = int(input("Check number for prime: "))
    checkPrime(num)
    printPrimes('EvanJacksonH2.txt')

if __name__ == '__main__':
    main()