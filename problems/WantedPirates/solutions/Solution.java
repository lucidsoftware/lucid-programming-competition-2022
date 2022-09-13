import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numLines = scanner.nextInt();
        scanner.nextLine(); // burn new line

        ArrayList<HashSet<String>> allPirates = new ArrayList<>();
        int smallestIndex = 0;
        for (int i = 0; i < numLines; i++) {
            List<String> line = Arrays.asList(scanner.nextLine().split(","));

            allPirates.add(new HashSet<String>(line));
            if (line.size() < allPirates.get(smallestIndex).size()) {
                smallestIndex = i;
            }
        }

        // algorithm
        for (Set<String> pirates : allPirates) {
            ArrayList<String> toRemove = new ArrayList<>();
            Set<String> smallest = allPirates.get(smallestIndex);
            for (String pirate : smallest) {
                if (!pirates.contains(pirate)) {
                    toRemove.add(pirate);
                }
            }
            for (String pirate : toRemove) {
                smallest.remove(pirate);
            }
        }

        Object[] output = (allPirates.get(smallestIndex).toArray());
        Arrays.sort(output);

        for (Object pirate : output) {
            System.out.println(pirate);
        }
    }
}