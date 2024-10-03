import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> unique_nums = new HashSet<>();
        
        unique_nums = Arrays.stream(nums)
                            .boxed()
                            .collect(Collectors.toSet());
        if (unique_nums.size() != nums.length){
            return true;
        }else{
            return false;
        }
    }
}