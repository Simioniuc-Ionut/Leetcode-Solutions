
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        // Cream un set de caractere unice pentru "jewels"
        Set<Character> unique_jewels = new HashSet<>();
        unique_jewels = jewels.chars().mapToObj(c -> (char) c).collect(Collectors.toSet());
        int c = 0;
        for(int i=0;i < stones.length(); i++){
            char w = stones.charAt(i);
            if (unique_jewels.contains(w)){
                c++;
            }
        }
        return c;
    }
}