#Hi! My name is Arlyn and this is my program Budget Helper. Budget Helper receives information from the user regarding his/her personal finances. It receives information such as the user's income and how much he/she spends monthly on housing, food, entertainment, etc. After the user enters all of the requested information, he/she is then brought to a menu where he/she has three options. The first option is to view two pie charts: one showing the user's spending and one showing the ideal budget. The second option is for an analysis, which tells the user what he/she is spending too much on and gives him/her tips on how to reduce spending in those areas. The third and last option is to end the program. I am assigned to Virtual Machine 45 and my email address is arlynr@bu.edu. I hope you enjoy the program!

print  "\nWelcome to the Budget Helper! \nHere to help you manage your budget and meet your financial goals!\nAnd don't worry: all of your information is kept confidential! \nWe will not share your personal financial information with anyone.\n"#Welcomes the user and tells him/her what the program does.
name = raw_input("To start, please enter your name: ") #Asks for the user's name and saves it in the variable name.

#Now we will ask Asks for the user's monthly net income.
try: #Here we are error-checking the user's input to see if it is a number. If it is not, they will be prompted to enter an number
        	income = float(raw_input("\nEnter your monthly net income (in USD): $ ")) 
	
except ValueError:
        	income= float(raw_input("You did not enter an number! \nPlease enter your salary in USD: "))

#Now we will ask the user how much he/she spends on differentr categories and save that number in its corresponding variable name.
#These values are error-checked to make sure they are numbers.
print "\nPlease tell me approximately how much you spend on each category a month (in USD).\n"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~SPENDING CATEGORIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
try:
	housing = int(raw_input("Housing (Rent/Mortgage): $ "))
except ValueError:
	housing = int(raw_input("You did not enter a number! \nPlease enter how much you spend on housing each month: $ "))
try: 
	utilities = int(raw_input("Utilities (Phone, Internet, Electricity, Gas, Water, etc): $ "))
except ValueError:
	utilities = int(raw_input("You did not enter a number! \nPlease enter how much you spend on utilities each month: $ "))
try:
	food = int(raw_input("Food (includes eating out): $ "))
except ValueError:
	food = int(raw_input("You did not enter a number! \nPlease enter how much you spend on food each month: $ "))
try:
	transportation = int(raw_input("Transportation: $ "))
except ValueError:
	transportation= int(raw_input("You did not enter a number! \nPlease enter how much you spend on transportation each month: $ "))
try:
	toiletries = int(raw_input("Toiletries/Essentials (soap, toilet paper, etc): $ "))
except ValueError:
	toiletries= int(raw_input("You did not enter a number! \nPlease enter how much you spend on toiletries each month: $ "))
try:
	entertainment = int(raw_input("Entertainment: $ "))
except ValueError:
	entertainment= int(raw_input("You did not enter a number! \nPlease enter how much you spend on entertainment each month: $ "))
try: 
	clothing = int(raw_input("Clothing: $ "))
except ValueError:
	clothing= int(raw_input("You did not enter a number! \nPlease enter how much you spend on clothing each month: $ "))
try:
	charity = int(raw_input("Charity(includes tithes and offerings): $ "))
except ValueError:
	charity= int(raw_input("You did not enter a number! \nPlease enter how much you spend on charity each month: $ "))
try:
	savings = int(raw_input("Savings/Retirement: $ "))
except ValueError:
	savings = int(raw_input("You did not enter a number! \nPlease enter how much you save each month: $ "))
try:
	other = int(raw_input("Other: $ "))
except ValueError:
	other = int(raw_input("You did not enter a number! \nPlease enter how much you spend on miscellaneous items each month: $ "))
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#Here we will see if the user is not spending more than his/her income. If he/she is, a warning will be displayed and the income will be changed to the total he/she spends in order to create the pie chart.
total = housing + utilities + food + transportation + toiletries + entertainment + clothing + charity + savings + other
overspending = False
if total > income:
	overspending = True
	diffover = int(total - income)
	income = float(total)
	print "-------------------------WARNING---------------------------"
	print ":    You are spending $%d more than you make!              :" %(diffover)
	print ": We will proceed using your total spending as your income. :" 
	print " ----------------------------------------------------------"
	contover = raw_input("\nPlease enter any key to continue onto the menu: ")

#Here we will convert the values for each spending category to a percentage of the total net income.
perchouse = housing/income * 100
percutil = utilities/income * 100
percfood = food/income * 100
perctransp = transportation/income * 100
perctoil = toiletries/income * 100
percentn = entertainment/income * 100
perccloth = clothing/income * 100
percchry = charity/income * 100
percsave = savings/income * 100
percother = other/income * 100
leftover = 100 - (perchouse + percutil + percfood + perctransp + perctoil + percentn + perccloth + percchry + percsave + percother)

#Here we have the "ideal" percentages for each category. This distribution is based on personal opinion and should not be taken as an "end all be all". Rather, it should be seen as a guide.
idealhouse = 30
idealutil = 10
idealfood = 10
idealtransp = 10
idealtoil = 2
idealentn = 5
idealcloth = 5
idealchry = 10
idealsave = 10
idealother = 3
idealleft = 5

#Now we will create a menu so the user can choose what he/she wants to do next.
mymenu = True #This boolean variable will keep our menu looping as long as it is True. It is switched to False only when the user chooses to end the program.
while mymenu == True:
	print "What would you like to do now? \nEnter the integer corresponding to what option you want.\n"
	print "     __________________________________________"
	print "    |                MENU                      |"                                   
	print "    | 1) View pie charts                       |"
	print "    | 2) View analysis and recommendations     |"
	print "    | 3) Exit Program                          |"
	print "    |__________________________________________|"
	
	try: #Here we are error-checking the user's input to see if it is an integer. If it is not, they will be prompted to enter an integer.
        	choice = int(raw_input("\nEnter 1, 2, or 3:  "))
	
	except ValueError:
        	choice = int(raw_input("You did not enter an integer! \nPlease enter 1 ,2, or 3: "))
	#If the user chooses option 1, they will view two pie charts: one of their budget and one of the ideal budget. This way, he/she can literally see how their spending matches up with the ideal model.
	if choice == 1:
		from pylab import *
		figure(1, figsize=(18,12)) #Creates our figure
		#Now we will create the labels for our pie slices, which are the different categories.
		labels = 'Other', 'Housing', 'Entertainment', 'Utilities', 'Charity','Food','Toiletries', 'Transportation', 'Clothing', 'Leftover','Savings'
		#Now we will wrote a list called fracs1, which will tell us what percent of the pie each corresponding category label takes up.
		fracs1 = [percother, perchouse, percentn, percutil, percchry, percfood, perctoil, perctransp, perccloth, leftover,percsave]
		mycolors=['red', 'blue', 'orange', 'magenta', 'cyan', 'yellow', 'green', '#FF9999','#99FF66', '#FF33CC', '#CC99FF']
		
		#Here we create the first pie chart - the user's pie chart - using the subplot function
		subplot(1,2,1)
		pie(fracs1, labels=labels, colors = mycolors, labeldistance = 1.15,
	                autopct='%1.1f%%', shadow=True)
		title("%s's Budget" %(name), bbox={'facecolor':'0.6', 'pad':8}) #The title of the pie chart will have the person's name in it!
		
		#This creates the second pie chart - the ideal one - next to the user's pie chart.
		subplot(1,2,2) 
		fracs2 = [idealother, idealhouse, idealentn, idealutil, idealchry, idealfood, idealtoil, idealtransp, idealcloth, idealleft, idealsave]

		pie(fracs2, labels=labels, colors = mycolors,labeldistance = 1.1,
	                autopct='%6.1f%%', shadow=True)

		title('Ideal Budget', bbox={'facecolor':'0.6', 'pad':8})

		
		show() #Displays the pie charts.

#If the user chooses option 2, they will be given an analysis of what he/she is spending too much on and be congratulated for main categories he/she is doing well in. If the user is spending too much in any category, the program will suggest ways to lower the cost in thos areas.

	elif choice == 2:
		print "\n\n"
		print "******************************* ANALYSIS & RECOMMENDATIONS ********************************"
		counter = 0 #This will keep track of all the categories the user is doing well on (i.e. not spending too much). This increments by 1 for each category the user is doing well on and if it is above a certain threshold (which here is 6) they are congratulated!
		if perchouse <= float(idealhouse)*(1.3): #Here we multily the idealhouse percentage by 1.3 to give the user some leeway (as the percentages are not set in stone). This factor is higher than the ones for the subsequent categories because housing is one of the expenses that is usually the most difficult to change.
			print "Your spending for housing is looking good!\n" 
			counter = counter + 1
		else:
			print "You are spending too much on housing. You may want to look into finding a place that is more affordable.\n"
		if percutil <= float(idealutil)*(1.2):
			print "Your spending for utilities is looking good!\n"
			counter = counter + 1
		else:
			print "Your utilities are too high. Consider buying energy-efficient appliances, unplugging electronics when they are not in use, taking shorter showers, or switching your telephone service provider.\n"
		if percfood <= float(idealfood)*(1.2):
			print "Your food spending is looking good!\n"
			counter = counter + 1
		else:
			print "You are spending too much on food. Consider eating out less often, brown-bagging your lunch, and using coupons when you go supermarket shopping.\n"
		if perctransp <= float(idealtransp) * (1.2):
			print "Your transportation costs are looking good!\n"
			counter = counter + 1
		else:
			print "You are spending too much on transportation. Try to reduce your spending by carpooling, taking public transportation, or riding a bike.\n"
 		if perctoil <= float(idealtoil) * (1.2):
			counter = counter + 1
		else:
			print "You are spending too much on toiletries. Consider buying soap, toilet paper, and paper towels in bulk to save money.\n"
		if percentn <= float(idealentn) * (1.2):
			counter = counter + 1
		else:
			print "You are spending too much on entertainment. Try to reduce your spending by renting or borrowing movies and video games or by spending time with friends at home.\n"
		if perccloth <= float(idealcloth) * (1.2):
			counter = counter + 1
		else:
			print "You are spending too much on clothing. Consider buying clothes from a thrift store or using a gentler cycle when washing your clothes to preserve them.\n"
		if percchry <= float(idealchry) * (1.2):
			counter = counter + 1
		else:
			print "You are spending too much on entertainment. Try to reduce your spending by renting or borrowing movies and video games or by spending time with friends at home.\n"
		if percother <= float(idealother) * (1.2):
			counter = counter + 1
		else:
			print "You are spending too much money on miscellaneous items.\n"


		if percsave < 10 and leftover < 10:
			print "You are not saving enough. Try to set some money aside each time you get your paycheck, even if it's a small amount. That way, you can build up an emergency fund then save for big events like vacations, weddings, and shopping sprees!\n"
		else:
			print "Good job! You are saving a good amount of money each month. Keep up the good work!\n"
			counter = counter + 1
		print "-------------------------------------------------------------------------------------------"
		#Congratulate the user if he or she did well in many categories, if he/she is not spending more than he/she makes.
		if counter >= 7 and overspending == False:
			print "             Congratulations! You are doing well on %d out of 10 categories!" %(counter)
		if overspending == True:
			print "                   SECOND WARNING: You are spending %d more than you make!" %(diffover)
		print "-------------------------------------------------------------------------------------------"
		print "*********************************** END OF ANALYSIS ****************************************"
		#We add the following part so that the menu does not immediately follow the user's analysis, which would make it confusing for the user to follow along (they would have to scroll up above the menu to see the analysis in this case). So we let the user press any key after he/she finishes reading to the analysis to continue on to the menu.
		cont = raw_input("\nPress any key to return to the menu: ")
		print "\n\n"

#If the user chooses option 3, the program ends since mymenu is changed to False, ending the while menu loop.
	elif choice == 3:
		print "\nThank you for checking out my program! Happy budgeting!\n"
		mymenu = False #This closes the program
#If the user enters an invalid entry that is an integer, it will not be caught by the try/except method above. So here we error-check the user's value to make sure that in the case that he/she enters any integer that is not 1,2, or 3, they will be shown an error-message and told to re-enter an option.
	else:
		#print "You have entered an invalid choice.\nPress any key to return to the menu.\n\n"	
		cont2 = raw_input("You have entered an invalid choice. Press any key to return to the menu: \n\n")
