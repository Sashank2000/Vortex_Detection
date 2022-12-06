import os

# Function to rename multiple files
def main():

    count = 1
    pwd = '/home/subhodeep/Documents/IIIT_Bangalore/Sem_3_2021/PE/Project/CNN Model/Train/images/dataset/down/'
    pwd2 = '/home/subhodeep/Documents/IIIT_Bangalore/Sem_3_2021/PE/Project/CNN Model/Train/images/dataset/data/down/'
    for count, filename in enumerate(os.listdir(pwd)):
        dst ="down" + str(count) + ".png"
        src = pwd + filename
        dst = pwd2 + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
