#!/usr/bin/node

const myMultiple = {
	myString1: "C is fun",
	myString2: "Python is cool",
	myString3: "JavaScript is amazing",
	myMethod: function() {
		return `${this.myString1}\nPython is cool\n${this.myString3}.`;
	}
};
console.log(myMultiple.myMethod());
