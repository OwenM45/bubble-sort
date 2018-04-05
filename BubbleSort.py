#read file
inputFile = open("DATA.txt","r")

#splits the file lines into an array
data = inputFile.readlines()

#counts how many times it loops through the list
loops = 0

#loops through the lines
for line in data:
    
    #splits the line into a list
    nums = line.split()

    #variable that checks if the list is sorted
    ordered = True

    #counter for while loop
    i = 0

    #loops through the list of numbers
    while i < len(nums):

        #try catch to find the end of the num list
        try:
            #checks if the first of the 2 is greater than the first 
            if int(nums[i]) > int(nums[i+1]):
                
                #sets temp variables for the first and second num
                firstNum = nums[i]
                secondNum = nums[i+1]

                #swaps the positions
                nums[i] = secondNum
                nums[i+1] = firstNum

                #sets ordered to false so the computer knows to loop again
                ordered = False                
                
        except:
            loops += 1
            if ordered == True:
                print(nums)
                print("It took " + str(loops) + " loops to sort")
                print("-------------------------------------------")
                break
            else:
                i = -1
                ordered = True
        i += 1
    
    
