class Solution {
    public boolean isAnagram(String s, String t) {
        String[] one = s.split("");
        String[] two = t.split("");

        Arrays.sort(one);

        Arrays.sort(two);

        if(s.length() != t.length())
        {
            return false;
        }

        for(int i = 0; i < one.length; i++)
        {
            if(!(one[i].equals(two[i]))){
                return false;
            }
        }
        return true;
    }
}
