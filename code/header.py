def initialize_data_root(user):
	if user == "AY":
		return("C:/Users/Andrew/1001-term-project/data/")
	if user == "AH":
		return("/Users/Alec/Documents/DSGA_1001_Homework/DSGA_1001_Final_Project/1001-term-project/data/")
	if user == "YZ":
		return("")
	else:
		return("Manually modify the data_root variable")

def world():
	print("Hello world")
	return()