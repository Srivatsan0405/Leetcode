class Solution {
    public static int lengthOfLongestSubstring(String s) {
        int l = 0, answer = 0;
        int[] chars = new int[128]; // For ASCII characters
        for (int i = 0; i < 128; i++) {
            chars[i] = -1; // Initialize with -1
        }

        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);
            if (chars[ch] >= l) {
                l = chars[ch] + 1;
            } else {
                answer = Math.max(answer, r - l + 1);
            }
            chars[ch] = r;
        }

        return answer;
    }
}