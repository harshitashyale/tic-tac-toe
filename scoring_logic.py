def sum(a, b, c):
    return a + b + c


def calculate_score(playerX, playerY):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    score_X = 0
    score_Y = 0
    for win in wins:
        if sum(playerX[win[0]], playerX[win[1]], playerX[win[2]]) == 3:
            score_X += 1
        if sum(playerY[win[0]], playerY[win[1]], playerY[win[2]]) == 3:
            score_Y += 1
    return score_X, score_Y


if __name__ == "__main__":
    playerX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerY = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Welcome to Tic-Tac-Toe Score Calculation")
    while True:
        print("Enter the moves of players (0-8 for each player) separated by spaces (e.g., '0 1 2 4 7 8'):")
        moves_X = list(map(int, input("Moves for X: ").split()))
        moves_Y = list(map(int, input("Moves for Y: ").split()))

        # Reset the players' boards
        playerX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        playerY = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Mark the moves on the board
        for move in moves_X:
            playerX[move] = 1
        for move in moves_Y:
            playerY[move] = 1

        score_X, score_Y = calculate_score(playerX, playerY)
        print("Score for Player X:", score_X)
        print("Score for Player Y:", score_Y)

        play_again = input("Do you want to calculate score again? (yes/no): ")
        if play_again.lower() != "yes":
            break
