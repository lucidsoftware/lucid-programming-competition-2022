import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        //parse input
        Scanner scan = new Scanner(System.in);
        int length = scan.nextInt();
        int numQueries = scan.nextInt();
        //parse shoalSizes
        int[] shoalSizes = new int [length];
        for (int i = 0; i < length; ++i) {
            shoalSizes[i] = scan.nextInt();
        }

        //calculate prefix XOR array. Preface with 0 to make processing queries easier
        int[] preXOR = new int[length + 1];
        preXOR[0] = 0;
        for (int i = 0; i < length; ++i) {
            preXOR[i + 1] = preXOR[i] ^ shoalSizes[i];
        }

        //process queries
        for (int i = 0; i < numQueries; ++i) {
            int start = scan.nextInt();
            int end = scan.nextInt();
            System.out.println(preXOR[start - 1] ^ preXOR[end]);
        }
        return;
    }
}