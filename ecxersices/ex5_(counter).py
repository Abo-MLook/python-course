import  time

my_time = int(input("Enter time in second : "))
for x in range (my_time , 0 , -1): # range(start, stop, step)
    second = x % 60              # x = 90, then second = 30.
    minute = int(x / 60) % 60   # if x = 90, then minute = 1.
    hours = int(x / 3600)
    print(f"{hours:02}:{minute:02}:{second:02}")
    time.sleep(1)
