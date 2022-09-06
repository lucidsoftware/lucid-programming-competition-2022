package problems.ReefPopulations.solutions.java;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(new InputStreamReader(System.in));
        int n = in.nextInt();
        int q = in.nextInt();

        int[] a = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            a[i] = a[i-1] ^ in.nextInt();
        }

        for (int i = 0; i < q; i++) {
            int x = in.nextInt();
            int y = in.nextInt();
            System.out.println(a[y] ^ a[x-1]);
        }
    }
}