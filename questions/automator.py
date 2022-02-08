while True:
	i = str(input())
	
	canswers = str(input())
	answers1 = str(input())
	answers2 = str(input())
	answers3 = str(input())
	canswers = "-".join(canswers.split())
	answers1 = "-".join(answers1.split())
	answers2 = "-".join(answers2.split())
	answers3 = "-".join(answers3.split())
	send = i + '\n' + f"[{canswers}]" + answers1 + answers2 + answers3 + '\n'
	print(send)
	with open("questions.txt", "a") as f:
		f.writelines(send)
