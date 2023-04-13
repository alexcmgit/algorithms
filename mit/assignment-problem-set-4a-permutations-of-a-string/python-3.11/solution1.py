def get_permutations(sequence: str) -> list[str]:
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1: return [sequence]

    subsequences = get_permutations(sequence[1:])
    fixed = sequence[0]
    sequences: list[str] = []

    for subseq in subsequences:
        for i in range(0, len(subseq) + 1):
            sequences.append(subseq[0:i] + fixed + subseq[i:])

    return sequences
