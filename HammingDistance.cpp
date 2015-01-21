//This program finds the Hamming Distance between the ternary forms of two numbers, which are entered by the user in decimal form.
#include<iostream>
using namespace std;

int main()
{

	cout << "Enter two numbers between 0-100: "; //Asks the user to enter two numbers.
	int num1, num2;
	cin >> num1; //Stores the two numbers as num1 and num2.
	cin >> num2;

	//Now we will find the ternary representation for num1 and num2 using a while loop.
	int mod1, mod2; //These will be our ternary digits for num1 and num2, respectively.
	int counter = 0; //This counter will keep track of how many digits differ (our Hamming Distance).
	int num1ter = num1, num2ter = num2; //These will be the variables we use to find the ternary forms, as they will be divided by 3 multiple times.
	while ((num1ter > 0) || (num2ter > 0)) //This loop will continue as long as neither number equals 0 (keep dividing until both are 0).
		{
		mod1 = num1ter % 3; //This gives us each ternary digit for num1 and num2.
		mod2 = num2ter % 3;

			if (mod1 != mod2)
				{
				counter++; //Increments our counter by 1 each time the ternary digits differ.
				}

		num1ter = floor(num1ter / 3); //We have to round these down to an integer so we can continue the process of finding the ternary forms using mod 3.
		num2ter = floor(num2ter / 3);
		}
	//Our output statement
	cout << "Hamming distance between " << num1 << " and " << num2 << " when numbers are in ternary format is " << counter << "." << endl;
	return 0;
}


