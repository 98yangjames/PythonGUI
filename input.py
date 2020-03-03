
def main():
	flag = -1;

	while flag < 0:
		input1 = raw_input("Input: ")
		file = open("file1.ncc", "a")
		file.write(input1)
		file.write("\n")
		if(input1 == "M2"):
			flag = 1;
			file.close()

main()