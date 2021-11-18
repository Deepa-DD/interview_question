def nonDivisibleSubset(length_of_list):
    list_of_numbers=[]
    for number in range(length_of_list): # running loop till length_of_list
        Element=int(input(" Enter the element for list :   ")) # I am asking numbers from user for list_of_numbers
        list_of_numbers.append(Element)   # appending the Element for making a list
    count=0      # taking count for counting divisible pairs
    for num in list_of_numbers:    # running the loop till list_of_numbers
        for diviend in list_of_numbers:  # running this loop so that i can compare ahead 
            if diviend > num :    # comparing so that dividend will not make pair with previews number
                sum=num+diviend   # doing sum of pair
                if sum % divisor != 0:  # we ae checking here that the pair is divisible or not 
                    count+=1   # if pair is divisibe then count will increase by 1
    return 'the count of peirs which is not divisible by  divisor is :',count
length_of_list=int(input(" How long list you want :   ")) # taking legnth from user
divisor=int(input(" Enter the number for Divisor :   ")) # taking user input (divisor) so that i can check elememts is divisible by divisor or not
print(nonDivisibleSubset(length_of_list))


                