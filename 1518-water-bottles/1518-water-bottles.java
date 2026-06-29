class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int b=numBottles-1;
        int e=numExchange-1;
        return numBottles+(b/e);


    }
}