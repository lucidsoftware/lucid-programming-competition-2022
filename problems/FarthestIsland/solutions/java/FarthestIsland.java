package problems.FarthestIsland.solutions.java;

import java.util.*;

public class FarthestIsland {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        String[] moneyAndCoupons = sc.nextLine().split(" ");
        int money = Integer.parseInt(moneyAndCoupons[0]), coupons = Integer.parseInt(moneyAndCoupons[1]);

        int costsSize = Integer.parseInt(sc.nextLine());

        String[] costsStr = sc.nextLine().split(" ");
        int[] costs = new int[costsSize];
        for (int i = 0; i < costsSize; ++i) costs[i] = Integer.parseInt(costsStr[i]);
        
        sc.close();

        int farthestIsland = getMaxIsland(costs, money, coupons);
        System.out.println(farthestIsland);
    }

    public static int getMaxIsland(int[] costs, int money, int coupons) {

        // Stores the cost of we used a coupon for
        PriorityQueue<Integer> costWhenCouponsUsed = new PriorityQueue<>();

        for (int i = 0; i < costs.length; ++i) {

            // Always try to use a coupon
            costWhenCouponsUsed.add(costs[i]);

            if (costWhenCouponsUsed.size() > coupons) {
                // If we used more coupons than we had, get the smallest cost a coupon was used
                // for and pay for that with money instead
                money -= costWhenCouponsUsed.remove();
            }

            if (money < 0)
                return i; // If we used more money than we started out with then we cannot make this trip.
        }

        return costs.length;
    }
}