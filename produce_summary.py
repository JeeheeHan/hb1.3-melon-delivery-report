file_one = open("um-deliveries-20140519.txt")
file_two = open("um-deliveries-20140520.txt")
file_three = open("um-deliveries-20140521.txt")

def produce_summary(file_number):
    """Return log of delivery information"""
    for line in file_number:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    file_number.close()

print("Day 1")
produce_summary(file_one)
print("Day 2")
produce_summary(file_two)
print("Day 3")
produce_summary(file_three)
