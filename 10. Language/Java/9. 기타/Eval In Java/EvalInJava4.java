
/**
 *  Object -> String 으로 변경,
 *  거기에 Boolean을 통한 비교연산(eq, ne, gt, gte, lt, lte, )까지 구현
 */
import java.util.ArrayList;
import java.util.HashMap;

import java.math.BigDecimal;
import java.text.SimpleDateFormat;

public class EvalInJava4 {

    private static final String alphabetic = "abcdefghijklmnopqrstuvwxyz";
    private static final String numeric = "0123456789.";
    private static final String alphanumeric = alphabetic + numeric;
    private static final String operators = "=~<#>$&|*/+-"; // 계산 우선 순위 별 나열. 순서에 맞지 않을 경우 고장

    public static void main(String[] args) throws IllegalArgumentException {
        // 순수 연산
        System.out.println(solveNumericExpression("1+3*9"));

        System.out.println("========================================");

        // 기본 + 띄어쓰기 대응
        HashMap<String, String> values = new HashMap<>();
        values.put("x", "4");
        for (String key : values.keySet())
        {
            if (firstContainsOnlySecond(values.get(key), numeric + "*/+-")) {
                System.out.println("순수" + solveNumericExpression(values.get(key)));
            }
        }
        // System.out.println(solve("x-3", values));
        // System.out.println(solve("x- 3", values));
        // System.out.println(solve(" x -3", values));
        // System.out.println(solve("x - 3 ", values));

        System.out.println("========================================");

        // 다중 키
        HashMap<String, String> values2 = new HashMap<>();
        values2.put("x", "4");
        values2.put("y", "6.2");
        values2.put("z", "(1.2+0.5)*5");
        for (String key : values2.keySet()){
            if (firstContainsOnlySecond(values2.get(key), numeric + "()*/+-")) {
                System.out.println("순수" + solveNumericExpression(values2.get(key)));
                values2.put(key, solveNumericExpression(values2.get(key)));
            }
        }
        System.out.println(solve("x * ((y - 1) * (z+1.5))", values2));  // 꼭 모든 변수 다 쓸 필요도 없음       
        // System.out.println(solve("x * ((-y - 1) * (-z+10))", values2));  // 변수에 마이너스 붙이기1  
        // System.out.println(solve("x*-y", values2));  // 변수에 마이너스 붙이기2 

        System.out.println("========================================");

        // 비교연산
        HashMap<String, String> values3 = new HashMap<>();
        values3.put("a", "10");
        values3.put("b", "20");
        values3.put("c", "30");
        values3.put("d", "true");
        values3.put("x", "false");
        for (String key : values3.keySet()){
            if (firstContainsOnlySecond(values3.get(key), numeric + "()*/+-")) {
                System.out.println("순수" + solveNumericExpression(values3.get(key)));
            }
        }
        // System.out.println("-c=-30 : " + solve("-c=-30", values3));
        // System.out.println("c<20 : " + solve("c<20", values3));
        // System.out.println("(a+b+c)>60.5 : " + solve("(a+b+c)>60.5", values3));
        // System.out.println("(a*-b+c)==-170 : " + solve("(a*-b+c)==-170", values3));
        // System.out.println("d&&x : " + solve("d&&x", values3));
        // System.out.println("d&x : " + solve("d&x", values3));
        // System.out.println("d||x : " + solve("d||x", values3));
        // System.out.println("((( !((a==10)&&(b==20))||(c<30.5) ))) : " + solve("[{{( !((a==10)&&(b==20))||(c<30.5) )}}]", values3));
        // System.out.println("!d : " + solve("!d", values3));
        // System.out.println("!x : " + solve("!x", values3));
        // System.out.println("!(d) : " + solve("!(d)", values3));
        // System.out.println("!(d|x) : " + solve("!(d|x)", values3));
        // System.out.println("!(d&x) : " + solve("!(d&x)", values3));


        // System.out.println("========================================");

        // Todo
        HashMap<String, String> values4 = new HashMap<>();
        values4.put("a", "10*20");
        values4.put("b", "2022-01-03");
        values4.put("c", "2022-01-04");
        values4.put("t", "true");

        // 날짜 체크
        for (String key : values4.keySet()){
            if (isDate(values4.get(key)) == true) {
                values4.put(key, values4.get(key).replace("-", ""));
            }
        }

        // 순수연산체크
        for (String key : values4.keySet()){
            if (firstContainsOnlySecond(values4.get(key), numeric + "*/+-")) {
                System.out.println("순수" + solveNumericExpression(values4.get(key)));
                values4.put(key, solveNumericExpression(values4.get(key)));
            }
        }



        // System.out.println(solve("a", values4));  // 연산연산1
        // System.out.println(solve("a==200", values4));  // 연산연산2
        // System.out.println(solve("b==true", values4));  // 직접 Bool박기
        System.out.println(solve("t&!t", values4));  // 날짜 연산
        // 후위표기식 체크


        // 보조함수 체크중
        // System.out.println(splitByLettersAndNumbers("2*3"));
    }

    public static String solveNumericExpression(String expression) {
        return solve(expression, new HashMap<>());
    }

    public static String solve(String function, HashMap<String, String> values) {

        return solveBracketsFunction(function, function, values);
    }

    // 소, 중, 대괄호를 function의 형태로 hashmap에 넣고 괄호 없는 연산으로 변경
    // ex : a * (b+c) 를 a* x 로 변환하고 hashmap에 key : x, value b+c를 저장
    private static String solveBracketsFunction(String function, String motherFunction, HashMap<String, String> values)
            throws IllegalArgumentException {

        // 띄어쓰기 삭제
        function = function.replace(" ", ""); 

        // 비교연산자 및 오타 수정
        function = function.replace("&&", "&"); // and
        function = function.replace("||", "|"); // or
        function = function.replace("==", "="); // eq
        function = function.replace("!=", "~"); // ne1
        function = function.replace("<>", "~"); // ne2
        function = function.replace("<=", "#"); // lte
        function = function.replace(">=", "$"); // gte

        String openingBrackets = "({[";
        String closingBrackets = ")}]";
        int parenthesisIndex = 0;
        do {
            int position = 0;
            int openParenthesisBlockIndex = -1;
            String currentOpeningBracket = openingBrackets.charAt(parenthesisIndex) + "";
            String currentClosingBracket = closingBrackets.charAt(parenthesisIndex) + "";
            if (cntHowMany(currentOpeningBracket, function) != cntHowMany(currentClosingBracket, function)) {
                throw new IllegalArgumentException("잘못된 괄호 사용 : " + function);
            }
            while (position < function.length()) {
                if (function.substring(position, position + 1).equals(currentOpeningBracket)) {
                    openParenthesisBlockIndex = position;
                } else if (function.substring(position, position + 1).equals(currentClosingBracket)) {
                    String newKey = getNewKey(values);
                    // @@@ 재귀
                    values.put(newKey, solveBracketsFunction(
                            function.substring(openParenthesisBlockIndex + 1, position), motherFunction, values));
                    function = function.substring(0, openParenthesisBlockIndex)
                            + newKey
                            + ((position == function.length() - 1) ? ("") : (function.substring(position + 1)));
                    position = -1;
                }
                position++;
            }
            parenthesisIndex++;
        } while (parenthesisIndex < openingBrackets.length());
        return solveBasicFunction(function, motherFunction, values);
    }

    private static String solveBasicFunction(String function, String motherFunction, HashMap<String, String> values)
            throws IllegalArgumentException {

        int position;
        int operatorIndex = 0;
        String currentOperator;
        do {
            currentOperator = operators.substring(operatorIndex, operatorIndex + 1);
            // 1순위 op
            if (currentOperator.equals("*")) {
                currentOperator += "/";
                operatorIndex++;
                // 2순위 op
            } else if (currentOperator.equals("+")) {
                currentOperator += "-";
                operatorIndex++;
            }
            operatorIndex++;

            position = 0; // current operation의 position
            while (position < function.length()) {
                if (currentOperator.contains(function.substring(position, position + 1)) & position != 0) {
                    int firstTermBeginIndex = position;

                    while (firstTermBeginIndex > 0) {
                        if ((alphanumeric.contains("" + function.charAt(firstTermBeginIndex)))
                                & (operators.contains("" + function.charAt(firstTermBeginIndex - 1)))) {
                            break;
                        }
                        firstTermBeginIndex--;
                    }
                    if (firstTermBeginIndex != 0 && (
                            function.charAt(firstTermBeginIndex - 1) == '-'
                            | function.charAt(firstTermBeginIndex - 1) == '+'
                            | function.charAt(firstTermBeginIndex - 1) == '!')) {
                        if (firstTermBeginIndex == 1) {
                            firstTermBeginIndex--;
                        } else if (operators.contains("" + (function.charAt(firstTermBeginIndex - 2)))) {
                            firstTermBeginIndex--;
                        }
                    }
                    String firstTerm = function.substring(firstTermBeginIndex, position);

                    int secondTermLastIndex = position;
                    while (secondTermLastIndex < function.length() - 1) {
                        if ((alphanumeric.contains("" + function.charAt(secondTermLastIndex)))
                                & (operators.contains("" + function.charAt(secondTermLastIndex + 1)))) {
                            break;
                        }
                        secondTermLastIndex++;
                    }
                    String secondTerm = function.substring(position + 1, secondTermLastIndex + 1);

                    String result;
                    BigDecimal val1 = null;
                    BigDecimal val2 = null;
                    Boolean valBool1 = null;
                    Boolean valBool2 = null;
                    String str1 = solveSingleValue(firstTerm, values);
                    if ("true".equals(str1)) {
                        valBool1 = true;
                    } else if ("false".equals(str1)) {
                        valBool1 = false;
                    } else {
                        val1 = new BigDecimal(str1);
                    }

                    String str2 = solveSingleValue(secondTerm, values);
                    if ("true".equals(str2)) {
                        valBool2 = true;
                    } else if ("false".equals(str2)) {
                        valBool2 = false;
                    } else {
                        val2 = new BigDecimal(str2);
                    }

                    switch (function.substring(position, position + 1)) {
                        case "=": result = Boolean.toString(val1.compareTo(val2) == 0); break;
                        case "<": result = Boolean.toString(val1.compareTo(val2) < 0); break;
                        case "#": result = Boolean.toString(val1.compareTo(val2) <= 0); break;
                        case ">": result = Boolean.toString(val1.compareTo(val2) > 0); break;
                        case "$": result = Boolean.toString(val1.compareTo(val2) >= 0); break;
                        case "~": result = Boolean.toString(val1.compareTo(val2) != 0); break;
                        case "&": result = Boolean.toString(valBool1 && valBool2); break;
                        case "|": result = Boolean.toString(valBool1 || valBool2); break;
                        case "*": result = val1.multiply(val2).toString(); break;
                        case "/": result = val1.divide(val2).toString(); break;
                        case "+": result = val1.add(val2).toString(); break;
                        case "-": result = val1.subtract(val2).toString(); break;
                        default: throw new IllegalArgumentException("없는 연산자: " + currentOperator);
                    }

                    // 소규모 계산 결과 저장
                    String newAttribute = getNewKey(values);
                    values.put(newAttribute, result);
                    function = function.substring(0, firstTermBeginIndex) + newAttribute
                            + function.substring(secondTermLastIndex + 1, function.length());

                    // 해시맵 정리
                    deleteValueIfPossible(firstTerm, values, motherFunction);
                    deleteValueIfPossible(secondTerm, values, motherFunction);
                    position = -1;
                }
                position++;
            }
        } while (operatorIndex < operators.length());
        return solveSingleValue(function, values);
    }

    private static String solveSingleValue(String singleValue, HashMap<String, String> values)
            throws IllegalArgumentException {

        if ("true".equals(singleValue) || "false".equals(singleValue) || isBigDecimal(singleValue)) {
            return singleValue;
        } else if (firstContainsOnlySecond(singleValue, alphabetic)) {
            return getValueFromMap(singleValue, values);
        } else if (firstContainsOnlySecond(singleValue, alphanumeric + "+-!" + "=!<#>$")) {
            String[] composition = splitByLettersAndNumbers(singleValue);
            if (composition.length != 2) {
                throw new IllegalArgumentException("잘못된 표현식 : " + singleValue);
            } else {
                // 음수 체크
                if (composition[0].equals("-")) {
                    composition[0] = "-1";
                } else if (composition[1].equals("-")) {
                    composition[1] = "-1";
                } else if (composition[0].equals("+")) {
                    composition[0] = "+1";
                } else if (composition[1].equals("+")) {
                    composition[1] = "+1";
                }

                BigDecimal res;
                if (isBigDecimal(composition[0])) {
                    res = new BigDecimal(composition[0])
                            .multiply(new BigDecimal(getValueFromMap(composition[1], values)));
                    return res.toString();
                } else if (isBigDecimal(composition[1])) {
                    res = new BigDecimal(composition[1])
                            .multiply(new BigDecimal(getValueFromMap(composition[0], values)));
                    return res.toString();
                // not 계산
                } else if (composition[0].equals("!")) {
                    if ("true".equals(getValueFromMap(composition[1], values))) {
                        return "false";
                    } else if ("false".equals(getValueFromMap(composition[1], values))) {
                        return "true";
                    } else {
                        throw new IllegalArgumentException("잘못된 not: " + singleValue);
                    }
                } else {
                    throw new IllegalArgumentException("잘못된 표현식: " + singleValue);
                }
            }
        } else {
            throw new IllegalArgumentException("잘못된 표현식: " + singleValue);
        }
    }

    // Map에서 Value 가져가기
    private static String getValueFromMap(String variable, HashMap<String, String> values)
            throws IllegalArgumentException {

        String val = values.get(variable);
        if (val == null)
            throw new IllegalArgumentException("Map에 없는 변수: " + variable);
        return val;
    }

    // 첫번째 String이 두번째 String의 내용물로만 구성되어있나 확인
    private static boolean firstContainsOnlySecond(String firstString, String secondString) {
        for (int j = 0; j < firstString.length(); j++) {
            if (!secondString.contains(firstString.substring(j, j + 1))) {
                return false;
            }
        }
        return true;
    }

    // 해쉬맵에 괄호 내 계산을 input
    private static String getNewKey(HashMap<String, String> hashMap) {

        String alpha = "abcdefghijklmnopqrstuvwxyz";
        for (int j = 0; j < alpha.length(); j++) {
            String k = alpha.substring(j, j + 1);
            if (!hashMap.containsKey(k)) {
                return k;
            }
        }

        // 정 없으면 문자열 두 개 조합
        for (int j = 0; j < alpha.length(); j++) {
            for (int i = 0; i < alpha.length(); i++) {
                String k = alpha.substring(j, j + 1) + alpha.substring(i, i + 1);
                if (!hashMap.containsKey(k)) {
                    return k;
                }
            }
        }
        throw new NullPointerException();
    }

    // 데이터 타입 확인
    private static boolean isBigDecimal(String number) {
        try {
            new BigDecimal(number);
            return true;
        } catch (Exception ex) {
            return false;
        }
    }

    // 문자 숫자 분리
    private static String[] splitByLettersAndNumbers(String val) {
        ArrayList<String> response = new ArrayList<>();
        String searchingFor;
        int lastIndex = 0;

        // 첫 글자 타입으로 검색 시작 대상을 확인
        if (firstContainsOnlySecond("" + val.charAt(0), numeric + "+-!" + "=~<#>$")) {
            searchingFor = alphabetic + "=~<#>$";
        } else {
            searchingFor = numeric + "+-!";
        }

        // 달라지는 시점 = split 할 시점
        for (int j = 0; j < val.length(); j++) {
            if (searchingFor.contains(val.charAt(j) + "")) {
                response.add(val.substring(lastIndex, j));
                lastIndex = j;
                if (searchingFor.equals(numeric + "+-!")) {
                    searchingFor = alphabetic + "=!<#>$";
                } else {
                    searchingFor = numeric + "+-!";
                }
            }
        }
        response.add(val.substring(lastIndex, val.length()));
        return response.toArray(new String[response.size()]);
    }

    // Map 안쓰는 변수 정리
    private static void deleteValueIfPossible(String val, HashMap<String, String> values, String function) {
        if (values.get(val) != null && function != null && !function.contains(val)) values.remove(val);
    }

    // howManyOfThatString에 속한 inThatString 개수 : 괄호 갯수 판별에 사용
    private static int cntHowMany(String howManyOfThatString, String inThatString) {
        return inThatString.length() - inThatString.replace(howManyOfThatString, "").length();
    }

    // 날짜 형식의 value인지 체크
    public static boolean isDate(String checkDate) {
        try {
            SimpleDateFormat dateFormatParser = new SimpleDateFormat("yyyy-MM-dd");  // 검증할 날짜 포맷 설정
            dateFormatParser.setLenient(false); // false일경우 처리시 입력한 값이 잘못된 형식일 시 오류가 발생
            dateFormatParser.parse(checkDate); // 대상 값 포맷에 적용되는지 확인
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}