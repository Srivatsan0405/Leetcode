public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> rs = new ArrayList<>();
        bt(s, 0, 0, "", rs);
        return rs;
    }
    private void bt(String s, int i, int d, String ip, List<String> rs) {
        if (d == 4 && i == s.length()) {
            rs.add(ip.substring(0, ip.length() - 1)); 
            return;
        }
        if (d > 4) return;
        for (int j = i; j < Math.min(i + 3, s.length()); j++) {
            String p = s.substring(i, j + 1);
            if (Integer.parseInt(p) < 256 && (i == j || s.charAt(i) != '0')) {
                bt(s, j + 1, d + 1, ip + p + ".", rs);
            }
        }
    }
}
