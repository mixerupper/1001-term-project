data_root = ""

def initialize_data_root(user):
	global data_root

	if user == "AY":
		data_root = "C:/Users/Andrew/1001-term-project/data/"
	if user == "AH":
		data_root = "/Users/Alec/Documents/DSGA_1001_Homework/DSGA_1001_Final_Project/1001-term-project/data/"
	if user == "YZ":
		data_root = ""

	return("Initialized data root")

def world():
	print("Hello world")
	return()