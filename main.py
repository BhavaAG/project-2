import time
def prime_number(number):
    for i in range(number+1):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i,"prime number")
                time.sleep(5.0)
                break

prime_number(25)



