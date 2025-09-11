function isPalindrome(x: number): boolean {
    if (x < 0) return false;

    let strX = String(x);
    return strX === strX.split("").reverse().join("");
};