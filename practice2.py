#move all zeros to end of a list.
def move():
    zero=[]
    non_zeros=[]
    all=[]
    num=[0,5,0,3,8,0,2]
    for i in num:
        if i ==0:
            zero.append(i)
        else:
            non_zeros.append(i)
    for i in non_zeros:
        all.append(i)
    for i in zero:
        all.append(i)
    return all
print (move())

# move all negative numbers to the beginning of the list.
def negative():
    pos=[]
    neg=[]
    all=[]
    num =[4,-2,7,-5,0,3,-1]
    for i in num:
        if i <0:
            neg.append(i)
        else:
            pos.append(i)
    for i in neg:
        all.append(i)
    for i in pos:
        all.append(i)
    return all
print(negative())

#find all duplicates elements in a list.
def duplicates():
    count={}
    result=[]
    num=[2,5,3,2,8,5,10,8]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in count:
        if count[i]>1:
            result.append(i)
    return result
print(duplicates())

# find the element with the highest frequency.
def frequency():
    count={}
    num=[2,5,2,8,5,2,10,8]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    highest=0
    answer=0
    for i in count:
        if count[i]>highest:
         highest=count[i]
         answer=i
    return answer
print(frequency())

# find the longest word in a sentence.
def long():
    text="i love my own company"
    words=text.split() #sentence ko word ki list m badal deta h.
    longest=""
    for i in words:
        if len(i)> len(longest):
            longest=i
    return longest
print (long())

# find the second largest number in a list.
def seclarg():
    highest=float("-inf")
    second_highest=float("-inf")
    num=[10,5,8,20,15,20]
    for i in num:
        if i>highest:
            second_highest=highest
            highest=i
        elif i>second_highest and i!=highest:
            second_highest=i
    return second_highest
print(seclarg())

#find the second smallest unique number.
def secsmall():
    smallest= float("inf")
    second_smallest= float("inf")
    num=[7,3,5,3,9,1,5]
    for i in num:
        if i < smallest:
            second_smallest= smallest
            smallest=i
        elif i<second_smallest and i!=smallest:
            second_smallest=i
    return second_smallest
print(secsmall())

# find the first element that appears only once.
def once():
    count={}
    result=[]
    num=[4,2,7,2,4,9,7,10]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in num:
        if count[i]==1:
            result.append(i)
    return result
print(once())

#find the longest consecutive sequence of the same number.
def longest_consecutive():
    current=1
    longest=1
    num=[2,2,2,5,5,2,2,8]
    for i in range(1,len(num)):
        if num[i]==num[i-1]:
            current+=1
        else:
            current=1
        if current > longest:
            longest=current
    return longest
print(longest_consecutive())

# find the first repeated element.
def first_repeated_element():
    count={}
    num=[4,7,2,9,7,5,2]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in num:
        if count[i]>1:
          return i
    return "no repeated element."
print(first_repeated_element())

#first non-repeating element.
def first_non_repeating_element():
    count={}
    num=[4,2,4,5,2,7,5]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in num:
        if count[i]==1:
          return i
    return "there is no non_repeated element."
print(first_non_repeating_element())

#find the second repeated element.
def second_repeated_element():
    count={}
    num=[4,2,7,2,5,4,7]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    first=[]
    second=[]
    for i in num: # value chahiye
        if count[i]>1:
            second=first
            first=i
        elif i>second and i != first:
            second=i
    return second
print(second_repeated_element())

#maximum consecutive increasing elements count in a list.
def max_consecutive():
    count=1
    max=1
    num=[1,2,3,2,3,4,5,1]
    for i in range(1,len(num)): # index chahiye isliye humne range liya.
        if num[i]>num[i-1]:
            count+=1
        else:
            count=1
        if count>max:
            max=count
    return max
print(max_consecutive())

#find a smallest number and its index in a list.
def num():
    num=[8,3,6,2,9,4]
    smallest=min(num)
    position= num.index(smallest)
    return smallest,position
print(num())
#method 2
def num1():
    num=[8,3,6,2,9,4]
    smallest=num[0]
    index=0
    for i in range(1,len(num)):
        if num[i]< smallest:
           smallest=num[i]
           index=i
    return smallest,index
print(num1())

#form a new list by removing all the duplicates ,order should be same.
def newlist():
    num=[4,2,4,5,2,7,5,8]
    new_list=[]
    for i in num:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(newlist())

#find the pair of numbers whose sum is 10 in list.
def sum():
    num=[2,7,3,8,5,1]
    for i in range (len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==10:
                print(num[i],"+",num[j],"=10")

#print those elements only who comes twice.
def twice():
    count={}
    result=[]
    num=[2,5,2,7,5,8,5,9]
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in num:
        if count[i]==2 and i not in result:
         result.append(i)
    return result
print(twice())

# find first non reapting character in a string.
def non_repeating():
    text="programming"
    for i in text:
        if text.count(i)==1:
         return i
print(non_repeating())

# remove duplicate and make new string with same order.
text="programming"
result=""
for i in text:
    if i not in result:
        result+=i
print(result)

#count vowels in a string.
text="programming"
vowels="aeiou"
count=0
for i in text:
    if i in vowels:
        count+=1
print(count)

# count total characters in a string except space in a string.
text="hello world"
count=0
for i in text:
    if i !=" ":
        count+=1
print(count)

#find the highest frequency character in string,ignore space.
text="hello world"
max_count=0
result=""
for i in text:
    if i !=" ":
        count=text.count(i)
        if count >max_count:
            max_count=count
            result=i
print(result)

#write each character with its index.
text="python"
for i in range(len(text)):
    print(i,text[i])

#make a new list of making square of each elements in a list.
num=[4,7,2,9,5]
new=[]
for i in num:
    new.append(i**2)
print(new)

#find the sum of all odd numbers in a list.
num=[4,7,2,9,5,8,10]
total=0
for i in num:
    if i%2!=0:
       total+=i
print(total)

#find the sum of cumulative sum of elements in a list.
num=[2,3,4,5]
total=0
result=[]
for i in num:
    total+=i
    result.append(total)
print(result)

#difference between consecutive elements.
num=[10,15,12,20,18]
result=[]
for i in range(1,len(num)):
    difference=num[i]-num[i-1]
    result.append(difference)
print(result)

#find the maximum frequency character in string.
text="banana"
max_count=0
max_char=""
for i in text:
    count=text.count(i)
    if count>max_count:
        max_count=count
        max_char=i
print(max_char)

#count frequency of each character in a string.
text="banana"
frequency={}
for i in text:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

# check if a list is sorted.
num=[1,2,3,4,5]
sorted_list="true"
for i in range(1,len(num)):
    if num[i]<num[i-1]:
        sorted_list="false"
        break
if sorted_list:
    print("sorted")
else:
    print("not sorted")

#find the index of the largest number.
num=[4,9,7,3]
largest=num[0]
index=0
for i in range (1,len(num)):
    if num[i]>largest:
        largest=num[i]
        index=i
print(index)

#find the difference between the largest and smallest number.
num=[8,3,7,5,12,2]
largest=num[0]
smallest=num[0]
for i in num:
    if i >largest:
        largest=i
    if i <smallest:
        smallest=i
difference=largest-smallest
print(difference)

#replace all negative numbers in a list with zero.
num=[4,-2,6,-5,3,-1]
for i in range(len(num)):
    if num[i]<0:
        num[i]=0
print(num)

# count positive, negative and zero numbers separately.
num=[3,-2,0,5,-7,0,8,-1]
positive=0
negative=0
zero=0
for i in num:
    if i >0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1
print(positive,negative,zero)

#move all the even no. to the beginnig.
num=[3,8,5,2,7,4,4,9,6]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
result=even+odd
print(result)

#find the elements that are present in the first list not in the second list.
list1=[1,2,3,4,5]
list2=[2,4,6]
result=[]
for i in list1:
    if i not in list2:
        result.append(i)
print(result)

# check if the lists are the subset of eachother or not.
list1=[1,2,3,4,5]
list2=[2,4,5]
is_subset="true"
for i in list2:
    if i not in list1:
        is_subset="false"
        break
print(is_subset)

# find the first biggest no. of given no.
num=[3,5,8,9,2]
biggest=num[0]
for i in num:
    if i>biggest:
        biggest=i
print(biggest)

#find the sum of the numbers digit.
num=5832
total=0
while num>0:
    digit=num%10
    total+=digit
    num=num//10
print(total)

# total words count in sentence.
text="i am learning python"
words=text.split()
print(len(words))

#count the number of digits in a no. set.
num=5234
count=0
while num >0:
    num=num//10
    count+=1
print(count)

#find the shortest word in the sentence.
text="i am learning python"
words=text.split()
shortest=words[0]
for word in words:
    if len(word)<len(shortest):
        shortest=word
print(shortest)

#removing the space from the string.
text="hello world python"
result=""
for i in text:
    if i!=" ":
        result+=i
print(result)

#count uppercase and lowercase characters in the string.
text="PyThON"
upper=0
lower=0
for i in text:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(upper,lower)

#find the first vowel in the string.
text="python"
for i in text:
    if i in "aeiou":
        print(i)
        break

#find the last vowel in the string.
text="education"
last_vowel=""
for i in text:
    if i in "aeiou":
        last_vowel=i
print(last_vowel)

#replace all vowels from *.
text="python programming"
result=""
for i in text:
    if i in "aeiou":
        result+="*"
    else:
        result+=i
print(result)

# check that all characters are unique.
text="python"
unique="true"
for i in text:
    if text.count(i)>1:
        unique="false"
        break
print(unique)