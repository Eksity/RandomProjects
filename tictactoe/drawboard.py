# My first attempt.
# Can make any rectangular shape.

pipe = "|   "
dash = " ---"

def make_grid(c_num, r_num):
	dashes = dash*c_num
	pipes = pipe*c_num + "|"
	for i in range(r_num):
		print(dashes)
		print(pipes)
	print(dashes)

if __name__ == "__main__":
	c_num = int(input("How many columns? "))
	r_num = int(input("How many rows? "))
	make_grid(c_num, r_num)