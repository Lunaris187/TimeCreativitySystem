import numpy as np

Q = np.zeros((5, 5))
alpha, gamma, epsilon = 0.1, 0.95, 1.0

def get_reward(state):
    return 10 if state == 4 else -1

for _ in range(1000):
    state = np.random.randint(0, 5)
    action = np.random.randint(0, 5) if np.random.random() < epsilon else np.argmax(Q[state])
    next_state = (state + action) % 5
    reward = get_reward(next_state)
    Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
    epsilon = max(0.1, epsilon * 0.99)

with open('q_table.txt', 'w') as f:
    f.write("Gelernte Q-Tabelle (optimale Aktionen):\n" + str(Q))
