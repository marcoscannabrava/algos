/*
 * Largest Sum Contiguous Subarray
 * 
 * example 1:
 * array = [-2, -3, 4, -1, -2, 1, 5, -3]
 * max_subarray -> indices 2:6 => sum = 7
 * 
 * example 2:
 * array = [-1, -3, -2]
 * 
 * 
 * 
 * [-2, -3, 7, -7, -1, -2, 1, 5, -3]
 * 
 * https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
*/


// max value of the array sets 

// itterate across the array and keep track of the sum, every time the
// sum goes below 0 reset the current sum to 0
// return the max number you find



const maxSum = (arr) => {
    if (arr.length === 0) return 0;
    let globalMax = -Infinity;
    let currMax = 0;
    for(let i = 0; i < arr.length; i++){
      currMax += arr[i];
      if(currMax > globalMax){
        globalMax = currMax;
      }
      if(currMax < 0){
        currMax = 0;
      }
    }
    return globalMax;
  }
  
  