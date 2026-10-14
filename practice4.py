#find the longest sublist in which the sum of elements is equal to zero.
list=[2,-2,3,1,-4,5]
longest=[]
for i in range(len(list)):#start
    total=0
    for j in range(i,len(list)):#till
        total+=list[j]
        if total==0:
            current=list[i:j+1]
            if len(current)>len(longest):
                longest=current
print(longest)

#find the longest consecutive sequence where every next num is exactly +1.
lst = [4,5,6,10,11,15,16,17,18]
longest = []
current = [lst[0]]
for i in range(1, len(lst)):
    if lst[i] == lst[i - 1] + 1:
        current.append(lst[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [lst[i]]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist where all elements are different.
lst = [1,2,3,2,4,5,6,4,7]
current=[]
longest=[]
for i in range(len(lst)):
    if lst[i] not in current:
        current.append(lst[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[lst[i]]
    if len(current) > len(longest):
          longest = current
print(longest)

#Find the first element in a list that is greater than the sum of all elements
#  before it.
num=[2,3,5,12,4,20]
total=0
for i in range(1,len(num)):
    if num[i]>total:
        print(num[i])
        break
    total+=num[i]

#find the longest sublist whose elements have an equal diff.btw consecutive num.
num=[2,4,6,3,6,9,12,15,5]
current=[num[0]]
longest=[]
pre_diff=num[1]-num[0]
for i in range(1,len(num)):
    diff=num[i]-num[i-1]
    if diff==pre_diff:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i]]
    pre_diff=diff
    if len(current)>len(longest):
        longest=current
print(longest)

#find the longest sublist in which the  diff.btw consecutive num keeps inc.
num=[1,2,4,7,11,16,5,6,8]
current=[num[0]]
longest=[]
pre_diff=num[1]-num[0]
for i in range(1,len(num)):
    diff=num[i]-num[i-1]
    if diff>pre_diff:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i-1],num[i]]
    pre_diff=diff
    if len(current)>len(longest):
        longest=current
print(longest)
    
#find the longest sublist in which every element is greater than the sum of the 
#previous two elements.
num=[1,2,4,7,13,5,6,12,25]
current=[num[0],num[1]]
longest=[]
for i in range(2,len(num)):
    if num[i]>num[i-1]+num[i-2]:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i-1],num[i]]
    if len(current)>len(longest):
            longest=current
print(longest)
        
#find the longest sublist where the numbers alternate btw inc and dec.
num=[1,5,2,8,3,2,4,6]
current=[num[0],num[1]]
longest=[num[0],num[1]]
for i in range(len(num)-2):
    if (num[i]<num[i+1]>num[i+2]) or (num[i]>num[i+1]< num[i+2]):
          current.append(num[i+2])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i+1],num[i+2]]
    if len(current)>len(longest):
                longest=current
print(longest)

#find the longest sublist in which the sum of every 3 consecutive elements is even.
num=[2,4,6,1,3,5,2,4]
current=[num[0],num[1]]
longest=[]
for i in range(len(num)-2):
    if (num[i]+num[i+1]+num[i+2])%2==0:
         current.append(num[i+2])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i+1],num[i+2]]
if len(current)>len(longest):
     longest=current
print(longest)

#find the longest sublist in which every element is greater than the previous
#element by at least 2.
num=[1,3,5,6,8,10,11,14]
current=[num[0]]
longest=[]
for i in range(1,len(num)):
    if num[i]-num[i-1]>=2:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i]]
if len(current)>len(longest):
    longest=current
print(longest)

#find the longest sublist in which every element is at least 2 smaller than the
#previous element.
num=[20,18,16,15,13,10,12,9,7]
current=[num[0]]
longest=[]
for i in range(1,len(num)):
    if num[i-1]-num[i]<=2:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i]]
if len(current)>len(longest):
    longest=current
print(longest)

#find the longest sublist where every elements is greater than the previous element,
# and the inc is strictly getting large.
num=[1,2,4,7,11,16,5,7,10,14]
current=[num[0]]
longest=[]
pre_diff=num[1]-num[0]
for i in range(1,len(num)):
    diff=num[i]-num[i-1]
    if num[i]>num[i-1] and diff>pre_diff:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i-1],num[i]]
    pre_diff=diff
if len(current)>len(longest):
            longest=current
print(longest)   
        
#find the longest sublist where every next elements is greater than the previous
# element,but the diff btw consecutive elements must alternate between even and odd
num=[1,3,6,8,13,15,20,22]
current=[num[0]]
longest=[]
pre_diff=num[1]-num[0]
for i in range(1,len(num)):
    diff=num[i]-num[i-1]
    if num[i]>num[i-1] and diff%2!=pre_diff%2:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i-1],num[i]]
    pre_diff=diff
if len(current)>len(longest):
     longest=current
print(longest)   

#Find the longest sublist where the difference between consecutive elements keeps 
# alternating between positive and negative.
num = [2,5,3,8,4,7,2,6,10]
current=[num[0]]
longest=[]
pre_diff=num[1]-num[0]
for i in range(1,len(num)):
    diff=num[i]-num[i-1]
    if (diff>0 and pre_diff<0) or (diff<0 and pre_diff>0):
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i-1],num[i]]
    pre_diff=diff
    if len(current)>len(longest):
        longest=current
print(longest) 

#Find the longest sublist where every element is greater than the avg of all
#previous elements in that sublist.
num=[2,3,4,6,10,5,12,20]
current=[num[0]]
longest=[]
total=num[0]
for i in range(1,len(num)):
    avg=total/len(current)
    if num[i]>avg:
        current.append(num[i])
        total+=num[i]
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i]]
        total=num[i]
    if len(current)>len(longest):
            longest=current
    print(longest) 

#Find the longest sublist where every element is greater than the previous element
# but no two consecutive diff are equal.
num=[1,3,6,8,13,18,20,25]
current=[num[0]]
longest=[]
pre_diff=num[1]-num[0]
for i in range(1,len(num)):
    diff=num[i]-num[i-1]
    if num[i]>num[i-1] and diff!=pre_diff:
        current.append(num[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[num[i-1],num[i]]
    pre_diff=diff
if len(current)>len(longest):
    longest=current
print(longest) 
#way2 if want to compare all previous elements
num = [1,3,6,8,13,18,20,25]
current = [num[0]]
longest = []
for i in range(1, len(num)):
    if all(num[i] > x for x in num[:i]):
        current.append(num[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i]]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist where each element is greater than all the elements 
# that come before it in that sublist.
num = [2,5,3,7,6,10,4,12]
current = [num[0]]
longest = []
for i in range(1, len(num)):
    if all(num[i]>x for x in current):
        current.append(num[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i]]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist in which every new element is smaller than all the 
#elements that came before it in that sublist.
num=[20,15,17,12,10,11,8,5]
current = [num[0]]
longest = []
for i in range(1, len(num)):
    if all(num[i]<x for x in current):
        current.append(num[i])
    else:
        if len(current) > len(longest):
             longest = current
        current = [num[i]]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist in which every new element is greater than the avg of all
#previous elements in that sublist and the diff between consecutive elements are inc.
num=[1,3,6,10,15,8,12,17,23]
current = [num[0]]
longest = []
total=num[0]
pre_diff=num[1]-num[0]
for i in range(1, len(num)):
    avg=total/len(current)
    diff=num[i]-num[i-1]
    if num[i]>avg and diff>pre_diff:
        current.append(num[i])
        total+=num[i]
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i-1],num[i]]
        total=num[i]
    pre_diff=diff
if len(current) > len(longest):
     longest = current
print(longest)

#Find the longest sublist in which every element is greater than the previous
#element,and the difference between consecutive elements is always even.
num=[1,3,7,9,15,18,20,24]
current = [num[0]]
longest = []
pre_diff=num[1]-num[0]
for i in range(1, len(num)):
    diff=num[i]-num[i-1]
    if num[i]>num[i-1] and diff%2==0 and pre_diff%2==0:
        current.append(num[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i-1],num[i]]
    pre_diff=diff
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist in which the cumulative sum remains positive at every step
num=[2,-1,3,-2,4,-10,5,1]
current = [num[0]]
longest = []
sum=num[0]
for i in range(1, len(num)):
    sum+=num[i]
    if sum>0:
        current.append(num[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i]]
        sum=num[i]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist in which the product of all elements remains less than 50.
num=[2,3,4,2,5,1,6]
current = [num[0]]
longest = []
product=num[0]
for i in range(1, len(num)):
    product*=num[i]
    if product<50:
        current.append(num[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i]]
        product=num[i]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest sublist in which the sum of every two consecutive elements is
#greater than 10.
num=[7,5,8,3,9,2,10,1]
current = [num[0]]
longest = []
sum=num[0]
for i in range(1, len(num)):
    sum+=num[i]
    if sum>10:
        current.append(num[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [num[i]]
        sum=num[i]
if len(current) > len(longest):
    longest = current
print(longest)

#Find the longest contiguous sublist in which the no. of even and odd elements is equal.
num=[2,4,7,9,6,3,8,5,10]
balance = 0
first = {0: -1}
longest = []
for i in range(len(num)):
    if num[i] % 2 == 0:
        balance += 1
    else:
        balance -= 1
    if balance in first:
        start = first[balance] + 1
        current = num[start:i+1]
        if len(current) > len(longest):
            longest = current
    else:
        first[balance] = i
print(longest)
#way2
num = [2,4,7,9,6,3,8,5,10]
longest = []
for i in range(len(num)):
    even = 0
    odd = 0
    for j in range(i, len(num)):
        if num[j] % 2 == 0:
            even += 1
        else:
            odd += 1
        if even == odd:
            current = num[i:j+1]
            if len(current) > len(longest):
                longest = current
print(longest)

#Find the longest contiguous sublist that contains at most 2 distinct elements.
num=[1,2,1,2,3,3,2,2,4]
longest = []
for i in range(len(num)):
    current = []
    for j in range(i, len(num)):
        if num[j] not in current:
            if len(set(current)) == 2:
                break
        current.append(num[j])
        if len(current) > len(longest):
            longest = current
print(longest)

#Find the longest contiguous sublist in which no elements appears more than twice.
num=[1,2,1,3,2,1,4,4,5]
longest = []
for i in range(len(num)):
    current = []
    for j in range(i, len(num)):
        if current.count(num[j])<2:
            current.append(num[j]) 
        else:
            break
    if len(current) > len(longest):
        longest = current
print(longest)
    
#Find the longest contiguous sublist in which the diff between the max and min 
#element is at most 5.
num=[3,5,7,4,9,10,6,8,12]
longest = []
for i in range(len(num)):
    current = []
    for j in range(i, len(num)):
        current.append(num[j])
        if max(current)-min(current)<=5:
            if len(current)>len(longest):
                longest=current.copy()
        else:
            current.pop()
            break
print(longest)

#Find the longest contiguous sublist in which the sum of any two consecutive 
# elements is even.
num=[2,4,6,3,5,7,8,10]
current=[num[0]]
longest = []
for i in range(1,len(num)):
    if (num[i]+num[i-1])%2==0:
            current.append(num[i])
    else:
        if len(current)>len(longest):
             longest=current
        current=[num[i]]
if len(current)>len(longest):
    longest=current
print(longest)
#way2
num = [2,4,6,3,5,7,8,10]
longest = []
for i in range(len(num)):
    current = [num[i]]
    for j in range(i + 1, len(num)):
        if (num[j] + num[j-1]) % 2 == 0:
            current.append(num[j])
        else:
            break
        if len(current) > len(longest):
            longest = current
print(longest)

#Find the longest contiguous sublist in which every element is greater than the 
# previous element by at least 3.
num = [2,5,8,10,14,17,18,22]
longest = []
for i in range(len(num)):
    current = [num[i]]
    for j in range(i + 1, len(num)):
        if num[j] - num[j-1] >= 3:
            current.append(num[j])
        else:
            break
        if len(current) > len(longest):
            longest = current
print(longest)

#Find the longest contiguous sublist in which every element is greater than the 
# average of all previous elements in that sublist.
num = [2,4,7,11,16,5,12,20]
longest = []
for i in range(len(num)):
    current = [num[i]]
    total = num[i]
    for j in range(i + 1, len(num)):
        avg = total / len(current)
        if num[j] > avg:
            current.append(num[j])
            total += num[j]
        else:
            break
        if len(current) > len(longest):
            longest = current
print(longest)

#find the longest contiguous sublist in which: every element is greater than the previous
#element and consecutive differences should not repeat.
num = [2,5,9,12,17,23,26,31]
longest = []
for i in range(len(num) - 1):
    current = [num[i]]
    pre_diff = num[i + 1] - num[i]
    current.append(num[i + 1])
    for j in range(i + 2, len(num)):
        diff = num[j] - num[j - 1]
        if num[j] > num[j - 1] and diff != pre_diff:
            current.append(num[j])
            pre_diff = diff
        else:
            break
    if len(current) > len(longest):
        longest = current
print(longest)

#way2
num = [2,5,9,12,17,23,26,31]
longest = []
for i in range(len(num)):
    current = [num[i]]
    pre_diff = None
    for j in range(i + 1, len(num)):
        diff = num[j] - num[j-1]
        if num[j] > num[j-1] and (pre_diff is None or diff != pre_diff):
            current.append(num[j])
            pre_diff = diff
        else:
            break
    if len(current) > len(longest):
        longest = current
print(longest)

#Find the longest sublist where the consecutive differences alternate between even
# and odd.
num = [2,5,9,12,18,21,26]
longest=[]
for i in range(len(num)):
    current=[num[i]]
    pre_diff=num[i]-num[i-1]
    for j in range(i+1,len(num)):
        diff=num[j]-num[j - 1]
        if diff%2!=pre_diff%2:
            current.append(num[j])
            pre_diff=diff
        else:
            break
    if len(current) > len(longest):
        longest = current
print(longest)

# find the longest sublist where: avg of all previous elements and the diff btw consecutive
#keeps increasing.
num=[2,5,9,14,20,25,40]
longest=[]
for i in range(len(num)):
    current=[num[i]]
    pre_diff=num[i]-num[i-1]
    total=num[i]
    for j in range(i+1,len(num)):
        diff=num[j]-num[j - 1]
        avg=total/len(current)
        if diff>pre_diff and num[j]>avg:
            current.append(num[j])
            pre_diff=diff
            total=num[j]
        else:
            break
    if len(current) > len(longest):
        longest = current
print(longest)

#find the longest sublist whose sum is divisible by 3.
num = [2, 1, 4, 2, 6, 5, 3]
first = {0: -1}
sum = 0
longest = 0
start = 0
end = 0
for i in range(len(num)):
    sum += num[i]
    rem = sum % 3
    if rem in first:
        length = i - first[rem]
        if length > longest:
            longest = length
            start = first[rem] + 1
            end = i
    else:
        first[rem] = i
print(num[start:end+1])
#way2
num = [2, 1, 4, 2, 6, 5, 3]
longest=[]
for i in range(len(num)):
    current=[]
    total=0
    for j in range(i,len(num)):
        total+=num[j]
        current.append(num[j])
        if total%3==0:
            if len(current)>len(longest):
                longest=current.copy()
print(longest)

#find the longest sublist whose sum is equal to a given target.
num=[2,3,1,4,2,5,1]
target=7
longest=[]
for i in range(len(num)):
    current=[]
    sum=0
    for j in range(i,len(num)):
        sum+=num[j]
        current.append(num[j])
        if sum==target:
            if len(current)>len(longest):
                longest=current.copy()
print(longest)

#find the longest continuous sublist where max and min stays within a given limit.
num=[1,3,5,4,8,6,7]
limit=4
longest=[]
left=0
for right in range(len(num)):
    while max(num[left:right+1])-min(num[left:right+1])>limit:
        left+=1
    current=num[left:right+1]
    if len(current)>len(longest):
        longest=current.copy()
print(longest)

#Find the longest substring in which no character appears more than 2 times.
text = "aabbaccc"
longest = ""
current = ""
count = {}
for i in text:
    current += i
    count[i] = count.get(i, 0) + 1
    while count[i] > 2:
        remove = current[0]
        current = current[1:]
        count[remove] -= 1
    if len(current) > len(longest):
        longest = current
print(longest)

#Find the longest continuous sublist where consecutive differences alternate btw odd and even.
num=[3,5,2,6,4,8,1,7]
longest = []
for i in range (len(num)):
        current=[num[i]]
        pre_diff=None
        for j in range(i+1,len(num)):
            diff=num[j]-num[j-1]
            if pre_diff is not None and diff%2==pre_diff%2:
                break
            current.append(num[j])
            pre_diff=diff
            if len(current) > len(longest):
               longest = current.copy()
print(longest)

#find the longest continuous sublist where consecutive difference alternate btw odd and
#even, number of even and odd elements is equal and sublist should be continuous.
num=[2,5,3,8,6,7,4,9,5]
longes=[]
for i in range (len(num)):
    current=[num[i]]
    even=1 if num[i]%2==0 else 0
    odd=1 if num[i]%2!=0 else 0
    pre_diff=None
    for j in range(i+1,len(num)):
        diff=num[j]-num[j-1]
        if pre_diff is not None and diff%2==pre_diff%2:
                break
        current.append(num[j])
        if num[j]%2==0:
            even+=1
        else:
            odd+=1
        pre_diff=diff
        if len(current) > len(longest) and even==odd :
           longest = current.copy()
print(longest)

#give a list of a integers,find the maximum possible sum of a continuous sublist.
num=[-2,3,-1,5,-6,4]
max_sum=num[0]
current=num[0]
for i in range (1,len(num)):
    current=max(num[i],current+num[i])
    max_sum=max(max_sum,current)
    print(max_sum)

#find the second longest strictly inc continuous sublist.
num=[1,2,3,1,4,5,6,2]
length=[]
current=[num[0]]
for i in range (1,len(num)):
    if num[i]>num[i-1]:
        current.append(num[i])
    else:
        length.append(len(current))
        current=[num[i]]
length.append(len(current))
length.sort(reverse=True)
print(length[1])

#find the longest continuous sublist where elements increasing ,consecutive differences
#even,odd alternate and same diff should not repeat.
num=[2,4,7,11,14,18,21,25]
longest=[]
current=[num[0]]
pre_diff=None
user_diff=set()
for i in range (1,len(num)):
    diff=num[i]-num[i-1]
    if diff>0 and diff not in user_diff:
        if pre_diff is None or diff %2!=pre_diff%2:
            current.append(num[i])
            user_diff.add(diff)
            pre_diff=diff
        else:
            if len(current)>len(longest):
              longest=current.copy()
            current=[num[i]]
            user_diff=set()
            pre_diff=None
if len(current)>len(longest) :
    longest=current.copy()            
print(longest)















