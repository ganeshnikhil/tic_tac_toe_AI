import random
import pickle

# =============================
# GAME UTILITIES
# =============================

WIN_PATTERNS = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def print_board(board):
    symbols = {1: "X", -1: "O", 0: " "}
    print("\n")
    for i in range(9):
        print(symbols[board[i]], end="")
        if i % 3 != 2:
            print(" | ", end="")
        if i % 3 == 2 and i != 8:
            print("\n---------")
    print("\n")

def check_win(board, player):
    for a, b, c in WIN_PATTERNS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def available_moves(board):
    return [i for i in range(9) if board[i] == 0]

# =============================
# Q-LEARNING AGENT
# =============================

class QLearningAgent:
    def __init__(self, alpha=0.3, gamma=0.95, epsilon=0.3):
        self.Q = {}  # (state, action) -> value
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q(self, state, action):
        return self.Q.get((state, action), 0.0)

    def choose_action(self, state):
        moves = available_moves(list(state))

        # Exploration
        if random.random() < self.epsilon:
            return random.choice(moves)

        # Exploitation
        q_values = [(a, self.get_q(state, a)) for a in moves]
        max_q = max(q_values, key=lambda x: x[1])[1]
        best = [a for a, q in q_values if q == max_q]
        return random.choice(best)

    def update(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        future_q = 0

        next_moves = available_moves(list(next_state))
        if next_moves:
            future_q = max(self.get_q(next_state, a) for a in next_moves)

        self.Q[(state, action)] = old_q + self.alpha * (
            reward + self.gamma * future_q - old_q
        )

# =============================
# TRAINING
# =============================

def train(agent, episodes=10000):
    wins = losses = draws = 0

    for ep in range(1, episodes + 1):
        board = [0] * 9
        state = tuple(board)

        while True:
            # AI move
            action = agent.choose_action(state)
            board[action] = 1

            if check_win(board, 1):
                agent.update(state, action, 1, tuple(board))
                wins += 1
                break

            if not available_moves(board):
                agent.update(state, action, 0, tuple(board))
                draws += 1
                break

            # Opponent (random)
            opp_move = random.choice(available_moves(board))
            board[opp_move] = -1

            if check_win(board, -1):
                agent.update(state, action, -1, tuple(board))
                losses += 1
                break

            next_state = tuple(board)
            agent.update(state, action, 0, next_state)
            state = next_state

        # Decay exploration
        agent.epsilon = max(0.01, agent.epsilon * 0.999)

        if ep % 1000 == 0:
            print(f"Episode {ep} | W:{wins} L:{losses} D:{draws} | epsilon={agent.epsilon:.3f}")

    print("\nTraining finished.")
    print(f"Final stats → Wins: {wins}, Losses: {losses}, Draws: {draws}")

# =============================
# HUMAN vs AI
# =============================

def play_vs_ai(agent):
    board = [0] * 9
    print("\nYou are O (positions 0–8)")
    print_board(board)

    while True:
        # Human move
        move = int(input("Your move (0-8): "))
        if board[move] != 0:
            print("Invalid move.")
            continue
        board[move] = -1

        if check_win(board, -1):
            print_board(board)
            print("You win!")
            return

        if not available_moves(board):
            print_board(board)
            print("Draw!")
            return

        # AI move
        state = tuple(board)
        ai_move = agent.choose_action(state)
        board[ai_move] = 1

        print("\nAI move:")
        print_board(board)

        if check_win(board, 1):
            print("AI wins!")
            return

# =============================
# MAIN
# =============================

if __name__ == "__main__":
    agent = QLearningAgent()
    train(agent, episodes=10000)

    # Save model
    with open("q_table.pkl", "wb") as f:
        pickle.dump(agent.Q, f)

    print("\nPlay against the trained AI!")
    while True:
        play_vs_ai(agent)
        if input("Play again? (y/n): ").lower() != "y":
            break
