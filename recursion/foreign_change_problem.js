  /*
  Change in a Foreign Currency
  You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. For example, Canada has given up the 1-cent penny. 
  If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.
  Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. Both the denominations and target amount will be given in generic units of that currency.
  
  Signature
  boolean canGetExactChange(int targetMoney, int[] denominations)
  
  Input
  1 ≤ |denominations| ≤ 100
  1 ≤ denominations[i] ≤ 10,000
  1 ≤ targetMoney ≤ 1,000,000
  
  Output
  Return true if it's possible to receive exactly targetMoney given the available denominations, and false if not.
  
  
  Example 1
  denominations = [5, 10, 25, 100, 200]
  targetMoney = 94
  output = false
  Every denomination is a multiple of 5, so you can't receive exactly 94 units of money in this currency.
  
  Example 2
  denominations = [4, 17, 29]
  targetMoney = 75
  output = true
  You can make 75 units with the denominations [17, 29, 29].
  
  
  7,10
  [x,x,x,x,x,x,x,x,x,x,x,95]
  
  85 or 88
  
  
  
  denominations 
  
  5   90  85 80 75 70 ... 5 0
  10  
  25  
  50
  
  [5, 10, 25, 50]
  
  
  denominations[3,7]
  DP solution
  [95, 92, 89, 88, 86]
  
  
  
  // we want to know: what are all the variations of 3 and 7, which reduce to 0
  [
      3[95,  92, 89, 86]
      7[95,  88, 85, 82]
      10[95, 85, 82, 79]
    ]
*/
    
  const dp = (arr, target) => {
    
    let arrs = new Array(arr.length).fill([target]);
    let curr = target;
    while(curr > 0){
      let vertical = arrs[0].length - 1;
      let prevMax = -Infinity;
      let prevSlice = []
      for(let i = 0;i<arr.length;i++){
        prevSlice.push(arrs[i][vertical]);
      }
      prevMax = Math.max(...prevSlice);
      for(let j = 0; j < arr.length;j++){
        let currVal = prevMax - arr[j]
        if (currVal === 0) return true;
        arrs[j][vertical].push(currVal)
      }
      curr = prevMax;
    }
    return false;
  }
  
  
  
//   target and reduce until we hit 0 if possible
  
  
  // write a recursive function which subtracts a denomination or not and use backtracking as well.
  // permutations problem
  
  const isPossible = (arrOfD, target) => {
    if(arrOfD.length === 0) return false;
    if(target < 0) return false;
    // set some outer variables
    arrOfD.sort();
    const isItPossible = false;
    const helper = (val) => {
      // backtracking case
      if(val < arrOfD[0]){
        return;
      }
      // base cases
      if(val < 0) return;
      if(val === 0){
        // set outer var and return
        isItPossible = true;
      }
      for(let i = 0; i < arrOfD.length;i++){
        const currentDenomination = arrOfD[i];
        helper(val - currentDenomination);    
      }
    }
    helper(target);
    return isItPossible;
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  