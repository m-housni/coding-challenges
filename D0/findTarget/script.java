public class IterativeBinarySearch
{
   public static int binarySearch(int[] elements, int target) {
      int left = 0;
      int right = elements.length - 1;
      while (left <= right)
      {
         int middle = (left + right) / 2;
         if (target < elements[middle])
         {
            right = middle - 1;
         }
         else if (target > elements[middle])
         {
            left = middle + 1;
         }
         else {
            return middle;
         }
       }
       return -1;
   }

   public static void main(String[] args)
   {
      int[] arr1 = {-20, 3, 15, 81, 432};

      int index = binarySearch(arr1,81);
      System.out.println(index);
   }
}

public class RecursiveBinarySearch
{
  public static int recursiveBinarySearch(int[] array, int target, int start, int end)
  {
      int middle = (start + end)/2;
      // base case: check middle element
      if (target == array[middle]) {
          return middle;
      }
      // base case: check if we've run out of elements
      if(end < start){
          return -1; // not found
      }
      // recursive call: search start to middle
      if (target < array[middle]){
          return recursiveBinarySearch(array, target, start, middle - 1);
      }
      // recursive call: search middle to end
      if (target > array[middle]){
          return recursiveBinarySearch(array, target, middle + 1, end);
      }
      return -1;
  }

 public static void main(String[] args)
 {
    int[] array = { 3, 7, 12, 19, 22, 25, 29, 30 };
    int target = 25;
    int foundIndex = recursiveBinarySearch(array,target,0,array.length-1);
    System.out.println(target + " was found at index " + foundIndex);
 }
}

