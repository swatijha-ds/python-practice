#find the second highest unique no. from a list.
num=[10,5,8,10,3,8,7]
result=[]
for i in num:
    if num.count(i)==1:
        result.append(i)
first=float("-inf")
second=float("-inf")
for i in result:
     if i>first:
        second=first
        first=i
     elif i>second and i!=first:
        second=i
print(second)

#find the first element in a list that is greater than the element
#immediately after it.
num=[2,4,7,5,8,10]
for i in range (len(num)-1):
    if num[i]>num[i+1]:
        print(num[i])
        break

#find the longest consecutive sequence of increasing nums in a list.
#way1:
num=[1,2,3,7,8,10,11,12,13]
count=1
longest=1
end=0
for i in range (len(num)-1):
    if num[i+1]==1+num[i]:
        count+=1
    else:
        count=1
    if count>longest:
        longest=count
        end=i+1
start=end-longest+1
print(num[start:end+1])
#way2:
num=[1,2,3,7,8,10,11,12,13]
prsnt=[num[0]]
longest=[num[0]]
for i in range (1,len(num)):
    if num[i]==1+num[i-1]:
        prsnt.append(num[i])
    else:
        prsnt=[num[i]]
    if len(prsnt)>len(longest):
        longest=prsnt
print(longest)

#find the element that has the second highest frequency in a list.
num=[1,2,2,3,3,3,4,4]
freq={}
for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
highest=0
sechighest=0
for i in freq:
    if freq[i]>highest:
        sechighest=highest
        highest=freq[i]
    else:
        freq [i]>sechighest and i!=highest
        sechighest=freq[i]
print(sechighest)

#find the first element in a list whose frequency is exactly 1 and
#whose value is greater than 10
num=[5,12,7,15,12,18,9,15,20]
result=[]
for i in num:
    if num.count(i)==1 and i>10:
            result.append(i)
            print(result)
            break

#find the longest word in a sentence that contains at least one repeated
#character.
sentence="cat apple dog banana"
longest=""
word=sentence.split()
for i in word:
   for char in i:
       if i.count(char)>1:
           if len(i)>len(longest):
            longest=i
print(longest)

#find the longest substring without any repeated characters.
s = "abcabbbd"
current = ""
longest = ""
for i in s:
    if i in current:
        current = current[current.index(i) + 1:]
    current += i                                
    if len(current) > len(longest):
        longest = current
print(longest)
print(len(longest))

#find the longest consecutive sequence of the same char.in a strng
strg = "aaabbccccdde"
same = ""
longest = ""
for i in strg:
    if same == "" or i == same[-1]:
        same += i
    else:
        if len(same) > len(longest):
            longest = same
        same = i
if len(same) > len(longest):
    longest = same
print(longest)
print(len(longest))
#way2
strg = "aaabbccccdde"
count=1
largest=1
for i in range(len(strg)-1):
    if strg[i]==strg[i+1]:
        count+=1
    else:
        count=1
    if count > largest:
        largest=count
print(largest)

#find the first character in a str that appears exactly once.
strg="aabbcdd"
count=""
for i in strg:
    if strg.count(i)==1:
        count+=i
        print(count)
        break

#find the first element in a list that is greater than both its previous
# and next elements.
num=[2,5,8,6,10]
for i in range(1,len(num)):
    if num[i]>num[i-1] and num[i]>num[i+1]:
        print(num[i])
        break

#find the first element in a list that is greter than every element before it.
num=[3,5,2,8,6,10]
for i in range(1,len(num)):
    if num[i]>max(num[:i]):
        print(num[i])
        break

#find the first element in a list that is smaller than every element after it.
num=[8,6,7,5,10]
for i in range(1,len(num)):
    if num[i]<min(num[i+1:]):
        print(num[i])
        break

#find the smallest no. in a list that appears more than once.
num=[5,2,8,2,7,5,3]
s=num[0]
for i in num:
    if num.count(i)>1 and i<s:
        s=i
        print(i)

#find the largest number in a list that appears exactly twice.
num=[4,7,2,7,9,4,6,2,8]
larg=num[0]
for i in num:
    if num.count(i)==2 and i>larg:
        larg=i
        print(i)

#find the second smallest unique number in a list.
num=[5,2,8,2,1,5,3]
first=num[0]
second=num[0]
for i in num:
    if num.count(i)==1:
     if i<first:
        second=first
        first=i
    elif i<second and i!=first:
        second=i
        print(i)

#find the first number in a list that is smaller than the avg of all the no. 
#before it.
num=[10,20,15,30,12]
total=num[0]
for i in range(1,len(num)):
    avg=total/i
    if num[i]<avg:
        print(num[i])
        break
    total+=num[i]

#find the first number in a list that is greater than the avg of all the num 
#before it.
num=[10,20,40,15,50]
total=num[0]
for i in range(1,len(num)):
    avg=total/i
    if num[i]>avg:
        print(num[i])
        break
    total+=num[i]

#find the first number in a list that is greater than both the avg and previos no.
num=[10,20,15,30,25]
total=num[0]    
for i in range(1,len(num)):
    avg=total/i
    if num[i]>avg and num[i]>num[i-1]:
        print(num[i])
        break
    total+=num[i]

#find the first num in a list whose value is greater than the avg of all the numbers before
#it and whose value is even
num=[10,20,15,30,25,40]
for i in range(1,len(num)):
    totak=num[0]
    avg=total/i
    if num[i]>avg and num[i]%2==0:
        print(num[i])
        break
    total+=num[i]

#find the first num in a list whose value is greater than every numbers before
#it and appears only once in the list.
num=[3,5,4,8,8,10,7]
for i in range(1,len(num)):
    if num[i]>max(num[:1]) and num.count(num[i])==1:
        print(num[i])
        break

#find the first number in a list that is greater than the avg of all numbers before it and
# greAter than the num immediately before it.
num=[10,15,12,20,18,30]
total=num[0]
avg=total/i
for i in range(1,len(num)):
    if num[i]>avg and num[i]>num[i-1]:
        print(num[i])
        break
    total+=num[i]

#find the first number in a list that is smaller than the avg of all numbers after it and
# smaller than the num immediately after it.
num=[20,15,18,25,30]
total=num[-1]
avg=total/i
for i in range(1,len(num)):
    if num[i]<avg and num[i]<num[i+1]:
        print(num[i])
        break
    total+=num[-1]

#find the first number in a list that is greater than  all numbers before it and
# smaller than the avg of all num  after it.
num=[5,10,8,20,25]
total=num[-1]
avg=total/i
for i in range(1,len(num)):
    if num[i]>max(num[:i])and num[i]<avg:
        print(num[i])
        break
    total+=num[i]

#find the first num in a list that is greater than the avg of all num before it and smaller
#than the avg of all num after it.
num=[10,20,15,30,40]
total1=num[0]
total2=num[-1]
for i in range(1,len(num)):
    avg1=total1/i
    avg2=total2/i
    if num[i]>avg1 and num[i]<avg2:
        print(num[i])
        break
    total1+=num[i]
    total2+=num[i]

#find the first num in a list that is greater than every num before and after it.
num=[5,8,6,10,7,4]
for i in range(1,len(num)):
    if num[i]>max(num[:i]) and num[i]>max(num[i+1:]):
        print(num[i])
        break
    
#find the first num in a list that is smaller than every num before and after it.
num=[20,15,18,10,12,5,8]
for i in range(1,len(num)):
    if num[i]<min(num[:i]) and num[i]<min(num[i+1:]):
        print(num[i])
        break

