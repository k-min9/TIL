import java.util.*;

/**
 * java에서는 combination 계열 로직을 직접 만들어야함
 * [A, B, C], [1, 2], [X, Y] 같이 List<List<String>>을 받으면 각 List 당 하나씩만 골라서 
 * [A,1,X],[A,1,Y], ... , [C,2,Y]를 반납하는 comb 로직을 재귀 없이 만들어두자
 */
public class CombinationGenerator {

    public static List<List<String>> getAllCombinations(List<List<String>> lists) {
        List<List<String>> result = new ArrayList<>();
        result.add(new ArrayList<>());

        for (List<String> list: lists) {
            List<List<String>> tempResult = new ArrayList<>();
            // 기존 comb에 현 루프중 List 원소 추가
            for (List<String> partialList : result) {
                for (String element : list) {
                    List <String> newComb = new ArrayList<>();
                    for (String partialString : partialList) {
                        newComb.add(partialString);
                    }
                    newComb.add(element);
                    tempResult.add(newComb);
                }
            }
            result = tempResult;
        }

        return result;
    }

    public static void main(String[] args) {
        // 예시 입력
        List<List<String>> inputLists = new ArrayList<>();
        List<String> list1 = new ArrayList<>();
        list1.add("A");
        list1.add("B");
        inputLists.add(list1);

        List<String> list2 = new ArrayList<>();
        list2.add("1");
        list2.add("2");
        inputLists.add(list2);

        List<String> list3 = new ArrayList<>();
        list3.add("X");
        list3.add("Y");
        list3.add("Z");
        inputLists.add(list3);

        // 가능한 모든 조합을 얻어옴
        List<List<String>> combinations = getAllCombinations(inputLists);

        // 모든 조합을 출력
        for (List<String> combination : combinations) {
            System.out.println(combination);
        }
    }
}
