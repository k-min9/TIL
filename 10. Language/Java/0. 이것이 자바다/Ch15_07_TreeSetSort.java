package ch15;

import java.util.NavigableSet;
import java.util.TreeSet;

public class Ch15_07_TreeSetSort {
	public static void main(String[] args) {
		TreeSet<String> treeSet = new TreeSet<String>();
		treeSet.add("apple");
		treeSet.add("forever");		
		treeSet.add("description");
		treeSet.add("ever");
		treeSet.add("zoo");
		treeSet.add("base");
		treeSet.add("guess");
		treeSet.add("cherry");
		
		System.out.println("[c~f 사이의 단어]");
		//subset(시작객체, 시작객체포함여부, 끝 객체, 끝객체 포함여부)
		NavigableSet<String> rangeSet = treeSet.subSet("c", true, "f", true);
		for(String word : rangeSet) {
			System.out.println(word);
		}

	}
}
