import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.math.BigDecimal;

/**
 * 이번 학습의 핵심 DTO Generator
 * Hashmap을 주고 받는 메소드간에 Hashmap을 상속받은 Dto 클래스를 만들어 형태를 강제할 수 있다.
 */
public class DTOCreator {
    private static final String CLASS_NAME = "MyDto"; // 생성할 클래스명

    public static void main(String[] args) {
        KeyInfo[] keys = {
                new KeyInfo("name", String.class),
                new KeyInfo("age", Integer.class),
                new KeyInfo("price", BigDecimal.class),
                new KeyInfo("isActive", Boolean.class)  // null을 받을 수 있는 class여야한다. boolean 같은것 사용금지
        };

        String generatedCode = generateDTOClass(CLASS_NAME, keys);

        // 생성된 코드를 파일로 저장
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(new File(CLASS_NAME + ".java")))) {
            writer.write(generatedCode);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class KeyInfo {

        private final String name;
        private final Class<?> type;
      
        public KeyInfo(String name, Class<?> type) {
            this.name = name;
            this.type = type;
        }
      
        public String getName() {
            return name;
        }
      
        public Class<?> getType() {
            return type;
        }
      }

    public static String generateDTOClass(String className, KeyInfo[] keys) {
        StringBuilder sb = new StringBuilder();

        // package
        // sb.append("package com.example.dto;\n\n");

        // imports
        sb.append("import java.math.BigDecimal;\n");
        sb.append("import java.util.HashMap;\n");
        sb.append("import java.util.Map;\n\n");

        // class declaration
        sb.append("public class ").append(className).append(" extends HashMap<String, Object> {\n");

        // fields
        for (KeyInfo key : keys) {
            sb.append("    private ").append(key.getType().getSimpleName()).append(" ").append(key.getName()).append(" = null;\n");
        }
        sb.append("\n");

        // getters and setters
        for (KeyInfo key : keys) {
            // getter
            sb.append("    public ").append(key.getType().getSimpleName()).append(" get").append(capitalize(key.getName())).append("() {\n");
            sb.append("        return ").append(key.getName()).append(";\n");
            sb.append("    }\n\n");

            // setter
            sb.append("    public void set").append(capitalize(key.getName())).append("(").append(key.getType().getSimpleName()).append(" ").append(key.getName()).append(") {\n");
            sb.append("        this.").append(key.getName()).append(" = ").append(key.getName()).append(";\n");
            sb.append("        this.put(\"").append(key.getName()).append("\", ").append(key.getName()).append(");\n");
            sb.append("    }\n\n");
        }

        // constructor
        sb.append("    public ").append(className).append("(HashMap parent) {\n");
        sb.append("        super(parent);\n");
        // for (KeyInfo key : keys) {
        //     sb.append("        this.put(\"").append(key.getName()).append("\", null);\n");
        // }
        sb.append("    }\n\n");

        // validateKey
        sb.append("    private void validateKey(String key) {\n");
        sb.append("        switch (key) {\n");
        for (KeyInfo key : keys) {
            sb.append("            case \"").append(key.getName()).append("\":\n");
        }
        sb.append("                break;\n");
        sb.append("            default:\n");
        sb.append("                throw new IllegalArgumentException(\"Invalid key: \" + key);\n");
        sb.append("        }\n");
        sb.append("    }\n\n");

        // put
        sb.append("    @Override\n");
        sb.append("    public Object put(String key, Object value) {\n");
        sb.append("        validateKey(key);\n");
        sb.append("        return super.put(key, value);\n");
        sb.append("    }\n\n");

        // get
        sb.append("    @Override\n");
        sb.append("    public Object get(Object key) {\n");
        sb.append("        validateKey(key.toString());\n");
        sb.append("        return super.get(key);\n");
        sb.append("    }\n\n");

        // toString
        sb.append("    @Override\n");
        sb.append("    public String toString() {\n");
        sb.append("        StringBuilder sb = new StringBuilder();\n");
        sb.append("        sb.append(\"{\");\n");
        sb.append("        for (Map.Entry<String, Object> entry : this.entrySet()) {\n");
        sb.append("            sb.append(\"\\\"\").append(entry.getKey()).append(\"\\\": \").append(entry.getValue()).append(\", \");\n");
        sb.append("        }\n");
        sb.append("        sb.delete(sb.length() - 2, sb.length());\n");
        sb.append("        sb.append(\"}\");\n");
        sb.append("        return sb.toString();\n");
        sb.append("    }\n");

        // end of class
        sb.append("}\n");

        return sb.toString();
    }

    private static String capitalize(String str) {
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }
}
