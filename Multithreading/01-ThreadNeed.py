import time

def job_1():
    print("Job_1 Started")
    start = time.time()
    k = 0
    for i in range(10000):
        for j in range(10000):
            k = i + j
    end = time.time()
    total = end - start
    print("Job_1 Completed in",total)

def job_2():
    print("Job_2 Started")
    start = time.time()
    k = 0
    for i in range(10000):
        for j in range(10000):
            k = i + j
    end = time.time()
    total = end - start
    print("Job_2 Completed in", total)

def job_3():
    print("Job_3 Started")
    start = time.time()
    k = 0
    for i in range(10000):
        for j in range(10000):
            k = i + j
    end = time.time()
    total = end - start
    print("Job_3 Completed in", total)

start = time.time()
job_1()
job_2()
job_3()
end = time.time()
total = end - start
print("Total time taken is",total)
