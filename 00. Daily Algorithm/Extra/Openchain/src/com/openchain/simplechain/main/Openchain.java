package com.openchain.simplechain.main;

import java.security.Security;
import java.util.ArrayList;
import java.util.HashMap;

import com.google.gson.GsonBuilder;
import com.openchain.simplechain.core.Block;
import com.openchain.simplechain.core.Transaction;
import com.openchain.simplechain.core.TransactionOutput;
import com.openchain.simplechain.core.Wallet;
import com.openchain.simplechain.util.StringUtil;

/**
 * ��ü���� ������ �������� ���ظ� ���� ���� �������� �����ϰ� �ֽ��ϴ�.
 * 
 * @author comnic
 *
 */
public class Openchain {

	//blockchain ArrayList
	public static ArrayList<Block> blockchain = new ArrayList<Block>();
	public static HashMap<String, TransactionOutput> UTXOs = new HashMap<String, TransactionOutput>(); //list of all unspent transactions.
	
	//difficulty - ���ڰ� Ŭ���� ��ƴ�. target���� ��Ģ��.
	//3�̻��� �� �����ɸ��� �� �մϴ�. �ʱ⿡ 3���� �Ͻð� ���ڸ� ������ ���ø� ���ذ� �ǽǵ� �մϴ�.^^
	public static int difficulty = 3;
	public static float minimumTransaction = 0.1f;
	
	public static Wallet walletA;
	public static Wallet walletB;
	
	/**
	 * main
	 * @param arg
	 */
	public static void main(String[] arg){

		//Setup Bouncey castle as a Security Provider
		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider()); 
		
		//Create the new wallets
		walletA = new Wallet();
		walletB = new Wallet();

		walletA.generateKeyPair();
		walletB.generateKeyPair();
		
		//Test public and private keys
//		System.out.println("Private and public keys:");
//		System.out.println(StringUtil.getStringFromKey(walletA.privateKey));
//		System.out.println(StringUtil.getStringFromKey(walletA.publicKey));
		
		//�׽�Ʈ�� ���� Transaction����(WalletA -> walletB : 100)  
		Transaction transaction = new Transaction(walletA.publicKey, walletB.publicKey, 100, null);
		//������ Transaction�� �����մϴ�.
		transaction.generateSignature(walletA.privateKey);
		
		//������ Transaction�� �����մϴ�.
		System.out.println("Is this Transaction Verify? " + transaction.verifiySignature());
		

		//�ʱ� ���� ����ϴ�.
		blockchain.add(new Block("Genesis block", "0"));
		System.out.println("\nTrying to Mine Genesis block!");
		blockchain.get(0).mineBlock(difficulty);
		
		//���� ���� �����մϴ�.
		for(int i = 1 ; i <= 3 ; i++){
			blockchain.add(new Block("block " + i, blockchain.get(blockchain.size()-1).hash));
			System.out.printf("\nTrying to Mine block #%d", i+1 );
			blockchain.get(i).mineBlock(difficulty);
		}
		
		//��ü blockchain�� �������� üũ�մϴ�.
		System.out.println("\nBlockchain is Valid : " + isChainValid());
		
		//��ü ���� ����մϴ�.
		String blockchainJson = new GsonBuilder().setPrettyPrinting().create().toJson(blockchain);
		System.out.println("\nOpenchain Block list : ");
		System.out.println(blockchainJson);

	}
	
	/**
	 * blockchain�� ��ȿ���� üũ�մϴ�.
	 *  - ���� ���� hash�� ��ȿ�� ������ üũ�Ѵ�.
	 *  - ���� ���� hash���� �������� üũ�Ѵ�.
	 * @return
	 */
	public static Boolean isChainValid() {
		Block currentBlock; 
		Block previousBlock;

		//��ü ���� üũ�մϴ�.
		for(int i=1; i < blockchain.size(); i++) {
			currentBlock = blockchain.get(i);
			previousBlock = blockchain.get(i-1);
			
			//���� ���� hash�� �´��� üũ�մϴ�.
			if(!currentBlock.hash.equals(currentBlock.calculateHash()) ){
				System.out.println("Current Hashes not equal");			
				return false;
			}
			
			//���� ���� hash���� �������� üũ�մϴ�.
			if(!previousBlock.hash.equals(currentBlock.previousHash) ) {
				System.out.println("Previous Hashes not equal");
				return false;
			}
		}
		return true;
	}	
}