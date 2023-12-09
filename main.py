l = [84, 23, 99, 10]
# sorted(l)
# Using the sorted function is cheating! Because this is a tutorial guys!

# Bubble sort: O(n^2)
for i in range(len(l)):
  for j in range(i + 1, len(l)):
    t = l[i]
    l[i] = l[j]
    l[j] = t
print(l)

#And you can also sort the list backwards by changing the sign of the comparison operator! :o
for i in range(len(l)):
  for j in range(i + 1, len(l)):
    if l[i] < l[j]:
      t = l[i]
      l[i] = l[j]
      l[j] = t
print(l)
