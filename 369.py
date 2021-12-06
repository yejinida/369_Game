# 369.py
# 컴퓨터는 절대 틀리지 않고 나만 틀린다는 가정..
printList = [] # 출력을 위한 리스트
saveList = [] # 단순히 수의 저장을 위한 리스트

def check369(value): # 숫자에 3, 6, 9 중 한 수가 들어있는지 판단하는 함수
	for i in value:
		if (i == '3' or i == '6' or i == '9'):
			return True

	return False

while (1): # 무한 반복문
	userInput = input() # 사람의 입력(문자열로 입력받음)
	if (userInput == '0'): # 만약 0 이 들어가면 반복문 탈출
		print("게임이 끝났습니다.")
		break
	else: 
		if (len(saveList) == 0): 
			if (userInput != '1'): # 처음 입력한 수가 1이 아닐 때
				print("1 부터 입력해주세요")
				break;
			else: # 나중에 비교를 위해 사용자가 첫 수로 1을 입력했으면 2도 그냥 리스트에 넣어줌
				saveList.append(1)
				saveList.append(2)
				printList.append(str(1))
				printList.append(str(2))
				print(printList) # 출력용리스트 출력

		else :
			if (check369(userInput) == True): # 입력한 수에 3, 6, 9가 들어있는데 x가 아닌 그냥 수로 입력했을 때
				print("틀렸습니다.")
				break

			else:
				nextNum = saveList[-1] + 1 # 비교를 위한 저장용 리스트의 가장 마지막 값에 1을 더한 수 (사용이 반복됨으로 변수 선언)
				if (userInput == 'x'): # 사용자의 입력이 x일때
					if (check369(str(nextNum)) == True): # saveList에는 숫자만 저장되므로 그 수로 check369()를 했을 때 
					#True이면 올바르게 입력 한 것이므로 출력용 리스트에는 x를 넣고 저장용리스트에는 다음 수 그대로 넣기
						printList.append('x')
						saveList.append(nextNum)
						print(printList)

					else: # x가 아닌데 x를 넣은 경우 ex) 3, 6, 9가 하나도 안들어가는데 x로 입력한 경우
						print("틀렸습니다.")
						break

				else: # 입력이 x가 아닐 때 
					if (check369(userInput) == True): # x를 입력해야 하는데 수를 그대로 넣은 경우 ex) 3, 6, 9, 13...
						print("틀렸습니다.")
						break
					else:
						if (int(userInput) != nextNum): # 연속된 수가 아닐 때
							print("연속된 수를 입력하세요.")
							break
						else:
							printList.append(userInput)
							saveList.append(int(userInput))
							print(printList)

				nextNum = saveList[-1] + 1 # 여기부터 컴퓨터 입력 
				if (check369(str(nextNum)) == True): # 3, 6, 9 들어있으면 
					printList.append('x') # 출력용에는 x넣고
					saveList.append(nextNum) # 저장용에는 수 그대로 append
					print(printList)

				else:
					printList.append(str(nextNum))
					saveList.append(nextNum)
					print(printList)
