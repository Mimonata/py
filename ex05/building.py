import sys
import string

def counting(text: str) -> None:
	sum_up = 0
	sum_lo = 0
	sum_pu = 0
	sum_sp = 0
	sum_di = 0
	for x in text:
		if x.isupper():
			sum_up += 1
		elif x.islower():
			sum_lo += 1
		elif x in string.punctuation:
			sum_pu += 1
		elif x.isspace():
			sum_sp += 1
		elif x.isdigit():
			sum_di += 1
	print(
		f"The text contains {len(text)} characters:\n"
		f"{sum_up} upper letters\n"
		f"{sum_lo} lower letters\n"
		f"{sum_di} digits\n"
		f"{sum_pu} punctuation marks\n"
		f"{sum_sp} white spaces\n"
		)


def main():
	length = len(sys.argv)
	assert length <= 2, "too many args!"
	if length == 1:
		text = input("Input the text to parse: ")
		counting(text)
	else:
		counting(sys.argv[1])

if __name__ == "__main__":
	try:
		main()
	except AssertionError as e:
		print(e)
		sys.exit(1)
