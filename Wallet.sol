// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract Wallet {

    address public owner;
    uint private userBalance;
    uint public withdrawAmount;
    bool public canWithdraw;

constructor(address _owner) {
        owner = _owner;
    }


function setUserBalance(uint _userBalance) public {
    userBalance = _userBalance;
}

function getUserBalance() public view returns(uint) {
    if (msg.sender == owner) {
        return userBalance;
    }
}

function updateWithdraw() public {
    if (withdrawAmount > userBalance) {
        canWithdraw = false;
    } else {canWithdraw = true;}
}

}

/*
Kontrat Spesifikasyonu: 

State Variables: 

1.	Owner (kontrat sahibi, public)
2.	userBalance (kontrat bakiyesi, private)
3.	withdrawAmount (çekmek istediğimiz miktar, public)
4.	canWithdraw (çekimin geçerli olup olmadığı; True, False, public)

Functions:

1.	Constructor (Owner’ı kontratı deploy eden kişi yapmalı)
2.	withdrawAmount için bir setter fonksiyon
3.	userBalance için bir setter fonksiyon
4.	userBalance için bir getter fonksiyon (sadece Owner çağırabilmeli bu fonksiyonu, if statement kullanarak sağlanmalı bu kural)
5.	withdrawAmount’ı, userBalance ile kıyaslayıp canWithdraw’ı güncelleyecek fonksiyon 	

Fonksiyonlar doğru şekilde view ya da pure olarak etiketlenmeli.
*/

