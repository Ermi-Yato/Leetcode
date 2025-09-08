function isHappy(n: number): boolean {
    const visited = new Set<number>()
    while (n !== 1 && !(visited.has(n)) ) {
        visited.add(n)
        let sum = 0
        while (n > 0) {
            let digit = n%10
            sum += digit*digit
            n = Math.floor(n/10)
        }
        n = sum
        sum = 0
    }

    return n===1
};