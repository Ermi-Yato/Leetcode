function isPalindrome(x: number): boolean {
    // if (x < 0) return false;

    // let strX = String(x);
    // return strX === strX.split("").reverse().join("");
    // Numbers ending in 0 (except 0 itself) are not palindromes
    if (x < 0 || (x > 0 && x % 10 === 0)) {
        return false;
    }
    // Reverse half of the number and compare
    let reversedHalf: number = 0;
    while (reversedHalf < x) {
        reversedHalf = reversedHalf * 10 + (x % 10);
        x = Math.floor(x / 10);
    }

    return x === reversedHalf || x === Math.floor(reversedHalf / 10);
};