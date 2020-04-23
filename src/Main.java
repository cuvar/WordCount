import java.util.*;

public class Main {

    private static Frame frm;

    public static void main(String[] args) {
        frm = new Frame();
    }


    public static String[] count(String s) {
        TreeMap<String, Integer> frequency = new TreeMap<>();

        //get all words and split them
        String[] uneditedWords = s.split("(\\r\\n|\\r|\\n|\\s|['(),;.:]+)"); // |C-q|C-j split by


        //rearrange words to look nice
        ArrayList<String> editedWords = new ArrayList<>();
        for (String word : uneditedWords) {
            word = word.toLowerCase();

            //remove all symbols
            String w = word.replaceAll("[^-/§$%€a-zA-Z0-9]", "");
            if (w.equals("")) {
                editedWords.remove(w);
            } else if (w.equals("m")) {
                editedWords.add("am");
            } else if (w.equals("re")) {
                editedWords.add("are");
            } else {
                editedWords.add(w);
            }

        }

        //put words in hashmap
        for (String w : editedWords) {
            //int j = 1;
            boolean match = false;
            for (Map.Entry<String,Integer> me : frequency.entrySet()) {
                if(w.equalsIgnoreCase(me.getKey())) {
                    match = true;
                }
            }
            if(match) {
                frequency.put(w, frequency.get(w) + 1);
            }
            else {
                frequency.put(w, 1);
            }

        }


        //put HashMap in array for JList
        String[] list = new String[frequency.size()];
        int i = 0;
        for (HashMap.Entry me : frequency.entrySet()) {
            list[i] = me.getKey() + ": " + me.getValue();
            i++;
        }
        //sort list by quantity
        list = sortByQuantity(list);

        return list;
    }



    public static String[] sortByQuantity(String[] arr) {
        int f1, f2;
        for (int i = arr.length - 1; i >=1; i--) {
            for (int j = 0; j < arr.length - 1; j++){
                String s1 = arr[j].substring(arr[j].lastIndexOf(":") + 2);
                String s2 = arr[j+1].substring(arr[j+1].lastIndexOf(":") + 2);
                f1 = Integer.parseInt(s1);
                f2 = Integer.parseInt(s2);
                if(f1 < f2){
                    String h = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = h;
                }
            }
        }
        return arr;
    }
}
