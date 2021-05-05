
# import EEGReadData as erd

er1 = er2 = er3 = er4 = er5 = 0

def get():
    global er1, er2, er3, er4, er5
    return er1, er2, er3, er4, er5

def seter(e1, e2, e3, e4, e5):
    global er1, er2, er3, er4, er5
    er1 = e1
    er2 = e2
    er3 = e3
    er4 = e4
    er5 = e5


for i in range(10):
    seter(i, (i+1),(i+2),(i+3),(i+4))
    me1, me2, me3, me4, me5 = get()
    print(me1, me2, me3, me4, me5)







'''
I need the CODE below. DO NOT DELETE IT
'''

# import threading
# import time
# x=0

# def task():
#     global x
#     while(x<400):
#         x+=1
#         print(x)
#         time.sleep(0.001)

# def task2():
#     global x
#     while(x<400):
#         print("\n")
#         print(x +1000)
#         time.sleep(0.3)
# def main_task():
#     t1 = threading.Thread(target=task)
#     t2 = threading.Thread(target=task2)
#     t1.start()
#     t2.start()

#     # t1.join()
#     t2.join()

# def main():
#     main_task()
#     print("{0}".format(x))

# main()