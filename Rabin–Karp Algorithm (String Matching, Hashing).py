def rabin_karp(text, pattern, prime=101):
    n, m = len(text), len(pattern)
    d = 256  # alphabet size
    h = pow(d, m-1) % prime
    p, t = 0, 0  # hash for pattern and text
    result = []

    # Preprocessing
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    # Sliding window
    for s in range(n-m+1):
        if p == t:  # possible match
            if text[s:s+m] == pattern:
                result.append(s)

        if s < n-m:
            t = (d*(t - ord(text[s])*h) + ord(text[s+m])) % prime
            if t < 0:
                t += prime

    return result


# Example
print("Rabin-Karp Match:", rabin_karp("abracadabra", "abra"))
