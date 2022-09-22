import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // parse real employees
        int numEmployees = Integer.parseInt(scan.nextLine());
        Set<String> realEmployees = new HashSet<>(numEmployees);
        for (int i = 0; i < numEmployees; i++) {
            // remove all white space and set lower case
            String realEmployee = scan.nextLine().replaceAll("\\s", "").toLowerCase();
            realEmployees.add(realEmployee);
        }

        int numCandidates = Integer.parseInt(scan.nextLine());
        for (int i = 0; i < numCandidates; i++) {
            // remove all white space and set lower case
            String candidateName = scan.nextLine().replaceAll("\\s", "").toLowerCase();
            if (realEmployees.contains(candidateName)) {
                System.out.println("EMPLOYEE");
            } else if (isBot(realEmployees, candidateName)) {
                System.out.println("BOT");
            } else {
                System.out.println("CUSTOMER");
            }
        }

    }

    private static boolean isBot(Set<String> realEmployees, String candidate) {
        for (String realEmployee : realEmployees) {
            int[] charFreq = new int[26];
            for (char c : realEmployee.toCharArray()) {
                charFreq[c-'a']++;
            }
            for (char c : candidate.toCharArray()) {
                charFreq[c-'a']--;
            }

            boolean offByOne = false;
            boolean isBot = true;
            for (int freq : charFreq) {
                if (freq > 1) {
                    isBot = false;
                } else if (Math.abs(freq) == 1) {
                    if (offByOne) isBot = false;
                    offByOne = true;
                }
            }

            if (isBot) {
                return true;
            }
        }
        return false;
    }
}
