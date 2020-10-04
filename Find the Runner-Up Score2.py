n = int(input())
arr = sorted(input().split())
final=list()
for i in arr:
x=int(i)
final.append(x)

high=max(final)


for i in final:

  if init is None :
      init=i
  if init==high:
      init=i
  elif i>init and i!=high:
      init=i
print(init)
