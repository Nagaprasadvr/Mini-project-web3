//SPDX-License-Identifier:UNLICENSED
pragma solidity >=0.6.0 <=0.9.0;

contract IpfsHashContract{
mapping(address=> string) public EthIpfs;
address payable public admin ;
uint256 payAmountinWei = 100000000000000;
constructor()
{
    admin = payable(0x9F7b18A0F6D25461a5F3FDD2Be2cb418022Ec63D);

}

function StoreIpfsHash(address payable sender,string memory IpfsHash)public payable {
payable(address(this)).send(payAmountinWei);
EthIpfs[sender] = IpfsHash;
require(sender.balance>=payAmountinWei);
admin.send(payAmountinWei);

}

function FetchIpfsHash(address user)public view returns(string memory){
    return (EthIpfs[user]);
}

function getContractBalance()public view returns(uint256){
    return payable(address(this)).balance;
}

function getAdminBalance()public view returns(uint256){
    return admin.balance;
}
}