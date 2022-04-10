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
