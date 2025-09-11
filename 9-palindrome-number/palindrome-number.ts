function isPalindrome(x: number): boolean {
    let y: string = String(x)
    let arrY: string[] = y.split("")
    let reversedY: string[] = arrY.reverse()
    let reversedStr: string = reversedY.join("")
    return parseInt(reversedStr) === x
};