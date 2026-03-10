class Solution {
    public boolean isPowerOfTwo(int n) {
        int c=0;
        while(n>0){
            if(n%2!=0){
                c+=1;
                n=n-1;
            }
            n=n/2;
        }
        return(c==1);


    }
}