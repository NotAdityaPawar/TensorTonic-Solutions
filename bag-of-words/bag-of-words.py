import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    hash_map = {}

    for token in tokens:
        hash_map[token] = hash_map.get(token, 0) + 1

    print(hash_map)

    ans = []

    for word in vocab:
        if word not in hash_map:
            ans.append(0)

        else:
            ans.append(hash_map[word])

    return np.array(ans, dtype = int)