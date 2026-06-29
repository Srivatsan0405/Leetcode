class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int b=numBottles;
        int e=numBottles;
        int nb;
        while (e>=numExchange){
            nb=e/numExchange;
            b+=nb;
            e = e % numExchange + nb ;
        }
        return b;


    }
}