# Coding conventions

## Core

* One tab to indent
* Opening brackets are always put directly next to the thing preceding them
* Closing brackets go on their own line
* Functions type, name, arguments and opening bracket all go on one single line
* No extra spaces on the insides of rounded brackets (function arguments, etc.) but a space between every function argument
* Spaces between operators, except for the increment and decrement operators
* All lower case for function and variable names
* All upper case for macro names
* No space after casting a type

Here's some valid code:
```c
int function(int a, bool secondarg){
	if(secondarg){
		a = a * 7;
	}
	else{
		a++;
	}
	return a;
}
```
