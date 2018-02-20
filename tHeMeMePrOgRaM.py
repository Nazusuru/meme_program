def input_or_file():
	which = input("Press f to read a file, i to enter input manually, or q to quit. ")
	while which != "q":
		while which != "f" and which != "i" and which != "q":
			which = input("Follow my instructions >( ")
		if which == "f":
			file()
		elif which == "i":
			manual()
		which = input("Press f to read a file, i to enter input manually, or q to quit. ")
	print("How dare you stop the meme you should've been rescinded.")

def file():
	file_opened = False
	while not file_opened:
		file_opened = True
		file_name = input("Type in your file name (without .txt!): ")
		try:
			file = open(file_name + ".txt", "r")
		except IOError:
			print("File doesn't exist you loser. ")
			file_opened = False
	memed = meme_it(file.read())
	memed_name = meme_it(file_name)
	output = open("memed_" + memed_name + ".txt", "w")
	output.write(memed)
	file.close()
	output.close()
	print("The meme has been done.")

def manual():
	to_be_memed = input("Type in the string to be memed: ")
	print(meme_it(to_be_memed))

def meme_it(line):
	upper_case = False
	memed = ""
	for i in range(len(line)):
		char = ord(line[i])
		if char > 64 and char < 91:
			if not upper_case:
				memed += chr(char + 32)
			else:
				memed += chr(char)
			upper_case = not upper_case
		elif char > 96 and char < 123:
			if not upper_case:
				memed += chr(char)
			else:
				memed += chr(char - 32)
			upper_case = not upper_case
		else:
			memed += line[i]
	return memed

input_or_file()