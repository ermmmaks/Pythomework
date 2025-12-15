import random
import math
from collections import deque

class WalkersAlias:
    def __init__(self, events_and_probs):
        if not events_and_probs:
            raise ValueError("Список событий пуст")

        self.events = [item[0] for item in events_and_probs]
        probs = [item[1] for item in events_and_probs]
        self.ln = len(self.events)

        if min(probs) < 0:
            raise ValueError("Вероятность не может быть отрицательной")
        
        result = sum(probs)
        if not(abs(result - 1.0) < 1e-6):
            raise ValueError("Сумма вероятностей должна быть близка 1")

        columns_probs = [p * self.ln for p in probs]

        self.alias_table = [-1] * self.ln
        self.prob_table = [0.0] * self.ln

        short = deque([i for i, p in enumerate(columns_probs) if p < 1.0])
        long = deque([i for i, p in enumerate(columns_probs) if p >= 1.0])

        while short and long:
            s = short.popleft()
            l = long.popleft()

            self.prob_table[s] = columns_probs[s]
            self.alias_table[s] = l

            columns_probs[l] -= (1.0 - columns_probs[s])

            if columns_probs[l] < 1.0:
                short.append(l)
            else:
                long.append(l)

        while short:
            self.prob_table[short.popleft()] = 1.0
        while long:
            self.prob_table[long.popleft()] = 1.0

    def get_random(self):
        e = random.randint(0, self.ln - 1)
        n = random.random()

        if n <= self.prob_table[e]:
            return self.events[e]
        else:
            return self.events[self.alias_table[e]]