// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

// 화폐 단위 : 소수점을 허용하지 않기 때문에 나눈다.
// 1 ether = 1e9 gwei = 1e18 wei
contract EtherUnits {
    uint public oneWei = 1 wei;
    uint public oneGwei = 1 gwei;
    uint public oneEther = 1 ether;
  
    // 1 wei is equal to 1
    bool public isOneWei = 1 wei == 1;

    bool public isOneEther1 = oneEther == 1e18;

    bool public isOneEther2 = oneEther == 10**9 * oneGwei;

    bool public isOneGwei = oneGwei == 10**9 * oneWei;
}