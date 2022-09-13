import java.util.*;

public class Main {

    public static void main(String[] args) {
        //parse input
        Scanner scan = new Scanner(System.in);
        int length = scan.nextInt();
        int[] wall = new int [length + 2];
        //add zeroes for the ends
        wall[0] = 0;
        wall[length + 1] = 0;
        for (int i = 0; i < length; ++i) {
            wall[i + 1] = scan.nextInt();
        }

        //check every index and the next 3 sections
        for (int i = 0; i < length + 1; ++i) {
            if (Math.abs(wall[i] - wall[i + 1]) > 4 ||
                (i < length && (Math.abs(wall[i] - wall[i + 2]) > 4)) ||
                (i < length - 1 && Math.abs(wall[i] - wall[i + 3]) > 4)) {
                    System.out.println("False");
                    return;
            }
        }
        System.out.println("True");
        return;
    }
}