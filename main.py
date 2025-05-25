first = []
second = []
third = []
count = 0
try:
   n = int(input())
   if 1 < n <= 50:
       m = int(input())
       if 0 <= m <= (n * (n - 1))/2:
           for i in range(m):
               a, b = input().split(" ")
               a = int(a)
               b = int(b)
               if a != b:
                   if 1 <= a <= n and 1 <= b <= n:
                       if a == 1:
                           first.append(b)
                       elif b == 1:
                           first.append(a)
                       if a != 1 and b != 1:
                           if a in first:
                               second.append(b)
                           elif b in first:
                               second.append(a)
                           if a not in first and b not in first:
                               if a in second:
                                   third.append(b)
                               elif b in second:
                                   third.append(a)
   second.pop(0)
   third.pop(0)
   for i in first:
       count += 1
   if count != 0:
       print("1 =>", first)
       count = 0
       for i in second:
           count += 1
       if count != 0:
           print("2 =>", second)
           count = 0
           for i in third:
               count += 1
           if count != 0:
               print("3 =>", third)
except:
   print()
