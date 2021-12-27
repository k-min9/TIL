package com.openchain.simplechain.core;

import java.util.Date;

import com.openchain.simplechain.util.StringUtil;

public class Block {

	public String hash;			/* �ؽð� */
	public String previousHash;	/* ���� ���� �ؽð� */
	private String data; 		/* ���� data */
	private long timestamp; 	/* timestamp */

	private int nonce;
	
	/**
	 * ���ο� ���� �����մϴ�.
	 * 
	 * @param data
	 * @param previousHash
	 */
	public Block(String data, String previousHash ) {
		this.data = data;
		this.previousHash = previousHash;
		this.timestamp = new Date().getTime();
		this.hash = calculateHash();	//������ ���� hash ���� �ϳ� ����� �־�Ӵϴ�.
	}
	
	/**
	 * ���ο� �ؽð��� �����մϴ�.
	 * @return
	 */
	public String calculateHash() {
		String calculatedhash = StringUtil.applySha256( 
				previousHash +
				Long.toString(timestamp) +
				Integer.toString(nonce) + 
				data 
				);
		return calculatedhash;
	}
	
	/**
	 * ä���մϴ�.
	 * 
	 * @param difficulty
	 */
	public void mineBlock(int difficulty) {
		//������ �׽�Ʈ�� ���ظ� �������� target�� difficulty ���� ��ŭ �տ� 0���� ä��ϴ�.
		String target = new String(new char[difficulty]).replace('\0', '0');
		
		//������ hash�� target�� �����ϸ� ä�� �����Դϴ�.
		//ex) difficulty�� 3�̸� target�� 000�� �ǰ�, ������ hash�� 000���� �����ϴ� ���̸� ä�� �����Դϴ�.
		//  ä���� ��� hash�� 000���� �����ϰ���...����
		while(!hash.substring( 0, difficulty).equals(target)) {
			nonce ++;
			hash = calculateHash();
			
			System.out.printf("\nGEN Hash #%d : %s", nonce, hash);
		}
		System.out.println("\nä�� ����!!! : " + hash);
	}
}