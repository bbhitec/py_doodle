##!/usr/bin/env python
'''
    @author [mst]
    @file   <filename>.<extension>    
    @brief  <title or quick description>
    full/optional description: this is a placeholder
    template for new files creation

    features, changelog:
    -2022.05: -initial draft

    @version 0.1 2022.05
'''



################## DRIVER
def main():
    print ("[mst] doodle")

    # challenge 2
    n = int(input().strip())
    if (n%2 == 1) or (n in range(6,21)):
        print("Weird")
    elif (n > 20) or (n in range(2,6)):
        print ("Not Weird")

    # challenge 3
    


if __name__ == ("__main__"):
    main()
