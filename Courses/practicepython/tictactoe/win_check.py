def check_win(arr):
    winner = 0
    #check rows
    for x in arr:
        if x[0] == x[1] and x[0] == x[2]:
            return x[0]
    #check columns
    if arr[0][0] == arr[1][0] and arr[0][0] == arr[2][0]:
        return arr[0][0]
    elif arr[0][1] == arr[1][1] and arr[0][1] == arr[2][1]:
        return arr[0][1]
    elif arr[0][2] == arr[1][2] and arr[0][2] == arr[2][2]:
        return arr[0][2]
	#check diagonals
    if arr[0][0] == arr[1][1] and arr[0][0] == arr[2][2]:
        return arr[0][0]
    elif arr[0][2] == arr[1][1] and arr[0][2] == arr[2][0]:
        return arr[0][0]
	
winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(check_win(no_winner))