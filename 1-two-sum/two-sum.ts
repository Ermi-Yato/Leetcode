function twoSum(nums: number[], target: number): number[] {
    const numIndexMap = new Map<number, number>()

    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]
        const difference = target - x

        if (numIndexMap.has(difference)) {
        return [numIndexMap.get(difference)!, i]
        }

        numIndexMap.set(x, i)
    }
    return []

};