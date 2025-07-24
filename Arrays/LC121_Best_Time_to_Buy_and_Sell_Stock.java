package Arrays;

public class LC121_Best_Time_to_Buy_and_Sell_Stock {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int min = prices[0];

        for (int i = 1; i < prices.length; i++) {
            int profit = prices[i] - min;

            if (profit < 0) {
                min = prices[i];
            } else if (profit > maxProfit) {
                maxProfit = profit;
            }
        }

        return maxProfit;
    }
}
