pragma solidity ^0.4.21;


contract Greeter{
    
    string public greeting;
    
    function Greeter() public {
        greeting = 'hello';
    }
    
    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    /* Main function */
    function greet() view public returns (string) {
        return greeting;
    }
    
}