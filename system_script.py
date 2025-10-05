import numpy as np
import subprocess
import sys
import os
from datetime import datetime

# 1. RL-Optimierung (Q-Learning)
print("=== RL-Optimierung: Q-Learning ===")
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
    f.write("Gelernte Q-Tabelle:\n" + str(Q))
print("Q-Tabelle gespeichert in q_table.txt")

# 2. Quanten-Simulation
print("\n=== Quanten-Simulation ===")
try:
    from qiskit import QuantumCircuit
except ImportError:
    print("Qiskit nicht gefunden. Installiere qiskit...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qiskit"])
    from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
with open('quantum_circuit.txt', 'w') as f:
    f.write("Quanten-Circuit:\n" + str(qc.draw()))
print("Quanten-Circuit gespeichert in quantum_circuit.txt")

# 3. Automatisierung (GitHub Actions Workflow wird bereits im Projekt angelegt)
print("\n=== Automatisierung: GitHub Actions ===")
print("Workflow ist in .github/workflows/main.yml definiert.")

# 4. Reddit-Post
print("\n=== Reddit-Post ===")
with open('reddit_post.txt', 'r') as f:
    print(f.read())

# 5. Pitch
print("\n=== Pitch-Dokument ===")
with open('pitch.txt', 'r') as f:
    print(f.read())

# 6. .gitignore
print("\n=== .gitignore ===")
with open('.gitignore', 'r') as f:
    print(f.read())

# 7. Hinweise für sicheren Git-Push
print("\n=== Hinweise für sicheren Git-Push ===")
print("Bitte nutze das Skript git_push.py und setze deinen GitHub-PAT als Umgebungsvariable GITHUB_TOKEN. Beispiel:")
print("  export GITHUB_TOKEN=dein_token")
print("  python git_push.py")

# 8. Hinweise für Reddit und Pitch
print("\n=== Reddit und Pitch ===")
print("1. Reddit: Öffne reddit_post.txt, poste in r/Entrepreneur oder r/test.")
print("2. Pitch: Kopiere pitch.txt in Google Doc (https://docs.google.com/), teile Link in GitHub-Issue ('Issues' > 'New Issue').")
print("3. Prüfe Actions: https://github.com/lunaris187/TimeCreativitySystem/actions")

print("\nSkript ausgeführt am: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
