import sys
def main():
    if len(sys.argv)!=2:
        sys.exit()
    else:
        print(f"square is {square(int((sys.argv[1])))}")
    
def square(num):
    return num+num

if  __name__ == "__main__":
    main()
