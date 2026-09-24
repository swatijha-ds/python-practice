# write a function named check_even_odd that takes oneinteger as input 
# and prints whether the no. is even or odd.
def check_even_odd(num):
    if num%2==0:
       print("this is an even num",num)
    else:
       print("this is an odd num",num)
(check_even_odd(5))

#write a function named find_largest(a,b) that returns the largest number.
def find_largest(a,b):
   if a>b:
      return(a)
   else:
      return(b)
print(find_largest(4,7))

#write a function named count_even(numbers) that returns the number of
#even numbers in a list.
def count_even():
   count=0
   numbers=[2,3,5,6,8,7]
   for i in numbers:
      if i%2==0:
         count=count+1
   return count
print(count_even())

#write a function find_sum(numbers) that returns the sum of all numbers
# in a list.
def find_sum():
   sum=0
   numbers=[2,5,7,1]
   for i in numbers:
      sum=sum+i
   return sum
print(find_sum())

#write a function count_odd(numbers) that returns the count of odd
# numbers in a list.
def count_odd():
   count=0
   numbers=[2,3,5,6,8,7]
   for i in numbers:
      if i%2!=0:
         count=count+1
   return(count)
print(count_odd())

#write a function find_smallest(numbers)that returns the smallest
#number in a list.
def find_smallest():
   numbers=[8,3,10,1,5]
   smallest=numbers[0]
   for i in numbers:
      if i<smallest:
         smallest=i
   return smallest
print(find_smallest())

#write a function find_second_largest(numbers) returns the largest
# number in a list.
def find_second_largest():
   number=[10,5,8,20,15]
   largest=number[0]
   second=number[0]
   for i in number:
      if i>largest:
         second=largest
         largest=i
      else:
         i>second and i !=largest
         second=i
   return second
print(find_second_largest())

#write a function that count vowels are present in a string.
def count_vowels():
   vowels="AEIOUaeiou"
   cv=0
   str=input("please enter your string:")
   for i in str:
      if i in vowels:
         cv=cv+1
   return cv
print(count_vowels())

#write a function that reverse a string.
def reverse_str():
   reverse=""
   str=input("pls enter your str:")
   for i in str:
      reverse=i+reverse
   return reverse
print(reverse_str())

#write a function to check whether a str is a palindrome.
def palindrome():
   reverse=""
   text=input("please enter your text value:")
   for i in text:
      reverse=i+reverse
   if text==reverse:
         return("yup, it is a alindrome.")
   else:
         return("nope, it is not a palindrome.")
print(palindrome())

#write a function to find the factorial of a number.
def factorial():
   fact=1
   numbers=int(input("please enter your number to find its factorial:"))
   for i in range(1,numbers+1):
      fact=fact*i
   return fact 
print(factorial())

#check whether it is a prime number or not:
def prime_number():
   num=int(input("please enter your num:"))
   if num <=1:
      return("it is not a prime number")
   for i in range(2,num+1):
      if num%i!=0:
         return("it is a prime number")
      else:
         return("it is not a prime number")
print(prime_number())

#count how many times a given number appears in a list.
def count():
   count=0
   target=2
   number=[1,2,3,5,3,4,2,5,6,1,7,5]
   for i in number:
      if i ==target:
         count=count+1
   return count
print(count())

# count how many times each number appears in a list.
def counting():
   count={}
   num=[7,6,8,5,6,6,8,4,5]
   for i in num:
      if i in count:
         count[i]+=1
      else:
         count[i]=1
   for key in count:
     print(key,";",count[key])
counting()

# remove duplicates from a list.
def remove_duplicates():
   result=[]
   num=[2,5,3,2,1,5,6,6]
   for i in num:
      if i not in result:
         result.append(i)
   return result
print(remove_duplicates())

#find the largest and smallest number in a list using one function.
def num():
   num= [8,7,6,5,4]
   largest=num[0]
   smallest=num[0]
   for i in num:
      if i>largest:
         largest=i
      else:
         i<smallest
         smallest=i
   return largest, smallest
l,s=num()
print(l,s)

#find the sum of all even numbers in a list.
def sum_even():
   sum=0
   num=[5,6,7,8,4,9,2]
   for i in num:
      if i%2==0:
         sum=sum+i
   return sum
print (sum_even())

#find the sum of all odd numbers in a list.
def sum_odd():
   sum=0
   num=[2,5,8,11,14,7]
   for i in num:
      if i%2!=0:
         sum=sum+i
   return sum
print(sum_odd())

#find the second smallest number in a list.
def second_smallest():
   num=[8,3,10,1,5]
   smallest= num[0]
   second=num[0]
   for i in num:
      if i<smallest:
         second=smallest
         smallest=i
      elif i<second and i!=smallest:
       second=i
   return second
print(second_smallest())
      
#check whether two strings are anagrams.
def anagrams():
   str1=input("pls enter your str:")
   str2=input("pls enter youe str:")
   if sorted(str1)== sorted(str2):
         return("yes, it is a anagrams.")
   else:
          return("nope, it is not a anagrams.")
print(anagrams())
          
#find the frequency of each character in a str.
def frequency():
   frequency={}
   str=input("pls enter your str:")
   for i in str:
      if i  in frequency:
         frequency[i]=+1
      else:
         frequency[i]=1
   return frequency
print(frequency())
          
#find the second largest no. in a lst
def second_largest():
   num=[8,3,10,5]
   largest=num[0]
   second=num[0]
   for i in num:
      if i>largest:
         second= largest
         largest=i
      elif i>second and i!=largest:
         second=i
   return second
print(second_largest())

#find the intersection of two list.
def intersection():
   repeat=[]
   list1=[1,2,3,4,5]
   list2=[3,4,5,6,7]
   for i in list1:
         if i in list2:
            repeat.append(i)
   return repeat
print(intersection())

#merge two list.
def merge():
   result=[]
   list1=[1,2,3]
   list2=[4,5,6]
   for i in list1:
      result.append(i)
   for i in list2:
      result.append(i)
   return result
print(merge())

#find a missing number in a list.
def missing():
   num=[1,2,3,5,6]
   for i in range(1,7):
      if i not in num:
       return i
print(missing())

#find the common elements from three lists.
def common():
   result=[]
   list1=[1,2,3,4,5]
   list2=[3,4,5,6]
   list3=[2,3,5,7]
   for i in list1:
      if  i in list2 and i in list3:
         result.append(i)
   return result
print(common())

#find the first non repeated element in a list.
def first_non_repeated():
   count={}
# step:1 count each number.
   num=[2,5,2,8,5,10]
   for i in num:
      if i in count:
       count[i]+=1
      else:
       count[i]=1
# step:2 count first non repeated number.
   for i in num:
      if count[i]==1:
         return i
   return "no unique element"
print(first_non_repeated())

#find the last non repeated element in a list.
def last_non_repeated():
   count={}
   num=[2,5,2,8,5,10]
   for i in num:
      if i in count:
         count[i]+=1
      else:
         count[i]=1
   for i in range(len(num)-1,-1,-1):
      if count[num[i]]==1:
       return num[i]
   return "no unique elements"
print(last_non_repeated())
      