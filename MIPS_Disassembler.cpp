 /*
  CS472 Computer Architecture
  Project 1 - MIPS Disassembler
   by Arlyn Rodriguez
  
  NOTES ON SHIFTS
 << shifts to the right (adds zeroes to the end) 2 << 4 gives us 100000 = 32
 >> shifts to the left (subtracts zeroes) 
 
 */
 #include <iostream>
 #include <string>
 using namespace std;


 void mainfunction(int address, unsigned int MIPSint)
 
 {
 
 // I. DIFFERENTIATE R-FORMAT AND I-FORMAT
 bool isRformat;
 
 if (MIPSint > 0x03FFFFFF) {//If first 6 bits are not zero (since this is the greatest value a 32-bit binary number cane be with 5 leading zeroes)
		 isRformat = false; //then we have I-format
	 }
	else 
		isRformat = true;
 
 
 //II. I-FORMAT CASE (loads and stores)
 if (!isRformat)
 {
	 short opcode;
	 unsigned int mask_opcode = 0b11111100000000000000000000000000;
     unsigned int opcode_extra = MIPSint & mask_opcode; //To be trimmed
	opcode = opcode_extra >>26; //Trims trailing zeroes to isolate opcode
	string opcodeString; 
	
		switch (opcode)
	{
		case 0b100000:
			opcodeString =  "add";
			break;
        case 0b100010:
	        opcodeString =  "sub";
			break;
		case 0b100100:
			opcodeString =  "and";  
			break;
		case 0b100101:
			opcodeString =  "or";
			break;
		case 0b101010:
			opcodeString =  "slt"; 
			break;
		case 0b100011:
			opcodeString =  "lw";
			break;
		case 0b101011:
			opcodeString =  "sw";
			break;
		case 0b000100:
			opcodeString =  "beq";
			break;
		case 0b000101:
			opcodeString =  "bne";
			break;
	}
	
	//string opcodeString = opcodeFinder(opcode);
	
	 short source1;
	 unsigned int mask_source1 = 0b00000011111000000000000000000000;
	 unsigned int source1_extra = MIPSint & mask_source1; //To be trimmed
	source1 = source1_extra >>21; //Trims trailing zeroes to isolate source1

	 short source2; //This is the destination for load (lw) commands
	 unsigned int mask_source2 = 0b00000000000111110000000000000000;
	 unsigned int source2_extra = MIPSint & mask_source2; //To be trimmed
	source2 = source2_extra >>16; //Trims trailing zeroes to isolate source2	
	
     short offset;
	 unsigned int mask_offset = 0b00000000000000001111111111111111;
	 offset = MIPSint & mask_offset; 
	
	//If the opcode was a branch command (beq or bne)
	if ( (opcode == 0b000100) || (opcode == 0b000101) )
	{
		int newoffset = offset << 2; //Shift to the right by two bits (adds two zeroes)
		int newaddress = address + newoffset; //To get address we are branching to
		
		//Print statements for beq or bne commands in assembly code
		cout << opcodeString << " $" << source1 << ", $" << source2 << ", " << hex << uppercase << newaddress <<endl;
	}
	else //If the opcode was not beq or bne
	{
		//Print statement for assembly code
		cout << opcodeString << " $" << source2 << ", " << offset << "($" << source1 << ")" <<endl;
	}
 
 } //Ends if statement/I-Format Case
 
 
//III. R-FORMAT CASE 
if (isRformat)
 {
	 short functcode;
	 unsigned int mask_functcode = 0b00000000000000000000000000111111;
    functcode = MIPSint & mask_functcode; //To be trimmed
	
	//Switch statement to get function code as string
	string functString;
		switch (functcode)
	{
		case 0b100000:
			functString =  "add";
			break;
        case 0b100010:
	        functString =  "sub";
			break;
		case 0b100100:
			functString =  "and"; 
			break;
		case 0b100101:
			functString =  "or";
		    break;
		case 0b101010:
			functString =  "slt";  
			break;
		case 0b100011:
			functString =  "lw"; 
			break;
		case 0b101011:
			functString =  "sw";  
			break;
		case 0b000100:
			functString =  "beq";
			break;
		case 0b000101:
			functString =  "bne";  
			break;
	}
	
	//Now we calculate each component
	
	 short source1; 
	 unsigned int mask_source1 = 0b00000011111000000000000000000000;
	 unsigned int source1_extra = MIPSint & mask_source1; //To be trimmed
	source1 = source1_extra >>21; //Trims trailing zeroes to isolate source1

	 short source2; 
	 unsigned int mask_source2 = 0b00000000000111110000000000000000;
	 unsigned int source2_extra = MIPSint & mask_source2; //To be trimmed
	source2 = source2_extra >>16; //Trims trailing zeroes to isolate source2

	short dest; 
	 unsigned int mask_dest = 0b00000000000000001111100000000000;
	 unsigned int dest_extra = MIPSint & mask_dest; //To be trimmed
	dest = dest_extra >>11; //Trims trailing zeroes to isolate destination
	
	//Prints assembly code
	cout << functString << " $"<< dest << ", $" << source1 << ", $"<< source2 << endl;
 } //Ends if statement/R-Format Case
 
} //End of mainfunction

int main() {

 int address = 0x7A060; //Initial address
 unsigned int myarray[11] = {0x022DA822, 0x8EF30018, 0x12A70004, 0x02689820, 0xAD930018, 0x02697824, 0xAD8FFFF4, 
0x018C6020, 0x02A4A825, 0x158FFFF6, 0x8E59FFF0}; //Array of hex instructions

for (int i = 0; i < 11; i++) //Loop through array of instructions and print out each line with address and assembly code
{
	cout << hex << uppercase << address << " " << dec;; //Print out address
	mainfunction(address, myarray[i]); //Call our mainfunction, which calculates and prints out assembly code
	address = address + 4; //Increment address by 4 each time (size of a word)
}

return 0;
} 

 
 
