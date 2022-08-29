// web3.js is used by the developers to use the ethereum network

// In the Case of Blockchain we want specific zeros at the starting of the hash because when the hash converted to a base 10 number it has be less than certain target number and therefore we want some zeros at the beginning to make it less than 0

// External Accounts are the accounts which are owned by an entity or humans and this can be a Metamask Account

// Like we know that we can use a External Account on various networks

// But a Contract Account is specific to a Particular Network

// The source code which we will write on our computer will act as a class and the code which will be deployed into the network will act as instance of that class
// Also we can deploy the same source code multiple times into the network

// navigator.geolocation.getCurrentPosition()

// A contract Account has a balance, data and the code which almost similar to machine code and cannot be understood by us

// let a=new Intl.NumberFormat('en-US').format(20)

// Car will be source code and the Mustang will be a Contract Account which has some data stored into it and this data can be retrived

// We write smart contracts in Solidity Language which has extension '.sol' and this is then compiled with Solidity compiler and then converted into two segments and one segment consits of the byte source code and another segment consits of Application Binary Interface (ABI)

// ABI acts as an Interface between Javascript and the Byte Code deployed into the Network and kind of it does a translation for the Javascript with some functions to interact with the data and also this is so plain that we can read and understand what the smart contract does

`
pragma solidity ^0.4.17;
// This is used to mention of the version of solidity we are using basically the compiler

contract Inbox{

    // Declaring a contract is similar to a class

    string public message;
    // string is used to define that it is going string into it
    // public acts as a access specifier
    // This are called as storage variables which are going to store the data whatever we give while deploying a instance into 
    // the network

    // There is other kind of variable which is called as local variable, they will be valid only till the 
    // execution of the contract and after that they are deleted


    function Inbox(string message_) public{
        message=message_;

        // This is known as constructor function which will be automatically called when an instance of this class
        // is created

    }

    function setMessage(string message_) public{
        message=message_;
    }

    function getMessage() public view returns (string){

        // public view is known to be as function type

        // Common function types
        // public : Anyone can call this function
        // private : Only the contract can call this function
        // view : this says that the function should return a data and it does not modify the contracts data
        // constant : this says that the function should return a data and it does not modify the contracts data
        // pure: Function will not read or even change the contracts data
        // payable : this is to declare a function when the user try to use this function and send ether along






        return message;
    }
}

`;

class Car {
  #pin = '1234';
  constructor() {
    this.Brand = 'Rolls';
  }

  get Name() {
    return this.Brand;
  }
}

Car.prototype.getName = function () {
  return this.Brand;
};

let car1 = new Car();

console.log(car1.pin);
console.log(car1.getName());
console.log(car1.getName);
