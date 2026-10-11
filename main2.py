input("Double loop at n = 4 took 10 steps. Watch it grow, Press enter")
for n in range(10, 100, 10):
   input("n " + str(n) + " Press Enter")
   print(" steps =", n * (n + 1) // 2)