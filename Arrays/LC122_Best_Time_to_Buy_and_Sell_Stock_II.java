package Arrays;

public class LC122_Best_Time_to_Buy_and_Sell_Stock_II {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int total = 0;

        for (int i = 1; i < prices.length; i++) {
            int profit = prices[i] - min;
            if (profit < 0) {
                min = prices[i];
            } else {
                total += profit;
                min = prices[i];
            }
        }

        return total;
    }
}
