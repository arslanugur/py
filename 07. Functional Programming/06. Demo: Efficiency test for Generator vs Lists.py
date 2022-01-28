import time

MAX_LIMIT = int(1e6+500) # try with different limits , note that for high numbers solo learn shows "No output." so, I highly recommand tesint on your local machine in you IDE
# the complilation time differs from machine to machine but try setting the Limit higher.
# I used Pycharm for testing, but I am posting on sololearn
class PrimeNumerTest:
    # implements eratostenes algorithm for detecting prime numbers
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes there is a wiki link with a easy to understand animation
    # the point is that the logic is the same the difference is yielding vs append
    def PrimeNumbersBasic(self):
        numbers = []
        primes = [False for i in range(MAX_LIMIT)]
        for i in range(2,MAX_LIMIT):
            if not primes[i]:
                numbers.append(i)
                for j in range(i * 2,MAX_LIMIT,i):
                    primes[j] = True
        return numbers

    def PrimeNumbersGenerator(self):
        primes = [False for i in range(MAX_LIMIT)]
        for i in range(2,MAX_LIMIT):
            if not primes[i]:
                yield i
                for j in range(i * 2,MAX_LIMIT,i):
                    primes[j] = True

    def RunTest(self):
        current_time = time.time()
        print("Starting prime number test")

        self.PrimeNumbersBasic()
        list_execution_time = time.time() - current_time

        print(f"Time elapsed using list {list_execution_time }")

        current_time = time.time()

        for _ in self.PrimeNumbersGenerator():
            pass
        generator_execution_time = time.time() - current_time
        print(f"Time elapsed using generator {generator_execution_time  }")
        
        if list_execution_time < generator_execution_time :
            print('So,List is faster')
        else:
            print('So,Generator is faster')
        print("===========\n")
class SimpleList:
    def BasicList(self):
        return [i for i in range(1,MAX_LIMIT)]
    def GeneratorList(self):
        for i in range(1,MAX_LIMIT):
            yield i
    def RunTest(self):
        current_time = time.time()
        print("Starting basic list test")

        self.BasicList()
        list_execution_time = time.time() - current_time

        print(f"Time elapsed using list {list_execution_time }")

        current_time = time.time()

        for _ in self.GeneratorList ():
            pass
        generator_execution_time = time.time() - current_time
        print(f"Time elapsed using generator {generator_execution_time  }")
        
        if list_execution_time < generator_execution_time :
            print('So,List is faster')
        else:
            print('So,Generator is faster')
        print("===========\n")
# Prime number test
prime_number_test = PrimeNumerTest()
prime_number_test.RunTest()

# Simple List tests
simple_list = SimpleList()
simple_list.RunTest()

