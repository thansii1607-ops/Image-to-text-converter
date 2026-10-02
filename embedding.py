import numpy as np


def create_embeddings(words):
    embeddings = []

    for word in words:
        vector = np.zeros(128)

        for i, char in enumerate(word.lower()):
            index = (ord(char) + i) % 128
            vector[index] += 1

        norm = np.linalg.norm(vector)

        if norm != 0:
            vector = vector / norm

        embeddings.append(vector)

    return np.array(embeddings)