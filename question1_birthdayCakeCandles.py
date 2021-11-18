def birthdayCakeCandles(age_of_user):
    candles_list=[]
    for age in range(age_of_user):      #running loop till age_of_user
        high_of_candles=int(input(" Enter high of Candles :   ")) # taking high of candles till user's age for candle_list
        candles_list.append(high_of_candles)      # appending for making a list of candle high
    maximum_high=0                           
    for high in candles_list:
        if high > maximum_high:     # comparing high with maximum_high
            maximum_high = high     # assingning the value for maximum_high, if peviews condition is true
    count_max_high=0                # taking variable called count_max_high for counting the maximum_high
    for count in candles_list:      # for excessing the element from the andles_list
        if count == maximum_high:  # checking and comparing if maximum_high is in the candles_list or not
            count_max_high+=1     #count increament if peviews condition is true
    return "The maximum height of candles we have :  ",maximum_high, "units high \nCount of highest candle :  ",count_max_high
age_of_user=int(input(" Enter birthday peson's age :  "))  # taking user input for defining length of list
print(birthdayCakeCandles(age_of_user ))




