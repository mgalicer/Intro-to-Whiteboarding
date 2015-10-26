
//This works for numbers greater than or equal to 0.

public int[] sum(int[] sum_pairs, int target){


  HashSet<Integer> set = new HashSet();
  int[] result = new int[2];

  for(int num : sum_pairs){

    if(set.contains(target - num)){
      result[0] = target - num;
      result[1] = num;
      return result;
    }
    set.add(num);
  }
  return result;
}
