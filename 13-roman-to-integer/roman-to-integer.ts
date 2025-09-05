function romanToInt(s: string): number {
    const romanInteger = {
    'I': 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }
    let value = 0

    for (let i = 0; i + 1 < s.length; i++) {
        const letter = s[i]
        if (romanInteger[letter] < romanInteger[s[i + 1]]) {
        value = value - romanInteger[letter]
        } else {
        value = value + romanInteger[letter]
        }
    }
    value = value + romanInteger[s[s.length-1]]
    return value
};