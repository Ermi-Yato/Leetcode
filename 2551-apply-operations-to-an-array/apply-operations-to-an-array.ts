function applyOperations(nums: number[]): number[] {
    const arrayLength: number = nums.length;
    for (let i = 0; i < arrayLength - 1; i++) {
        if (nums[i] === nums[i + 1]) {
            nums[i] = nums[i] << 1;
            nums[i + 1] = 0;
        }
    }
  
    const resultArray: number[] = Array(arrayLength).fill(0);
  
    let currentIndex: number = 0;
  
    for (const element of nums) {
        if (element !== 0) {
            resultArray[currentIndex] = element;
            currentIndex++;
        }
    }
  
    return resultArray;
};