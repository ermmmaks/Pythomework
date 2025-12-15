import random
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
            shrt = short.popleft()
            lng = long.popleft()

            self.prob_table[shrt] = columns_probs[shrt]
            self.alias_table[shrt] = lng

            columns_probs[lng] -= (1.0 - columns_probs[shrt])

            if columns_probs[lng] < 1.0:
                short.append(lng)
            else:
                long.append(lng)

        while short:
            self.prob_table[short.popleft()] = 1.0
        while long:
            self.prob_table[long.popleft()] = 1.0

    def get_random(self):
        xi = random.randint(0, self.ln - 1)
        eta = random.random()

        if eta <= self.prob_table[xi]:
            return self.events[xi]
        else:
            return self.events[self.alias_table[xi]]