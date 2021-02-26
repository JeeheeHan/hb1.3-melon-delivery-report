
def produce_summary(day, file_number):
    """Return log of delivery information
    
    Print out the Day number and the document details by 
    melon, count, and amount
    
    """

    print(f"Day {day}")     #Pass in arg for Day Num
    opened_file = open(file_number)   #declare var to close the file at the end
    
    for line in opened_file:      #opening file
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    opened_file.close()


produce_summary(1,"um-deliveries-20140519.txt")
produce_summary(2,"um-deliveries-20140520.txt")
produce_summary(3,"um-deliveries-20140521.txt")
