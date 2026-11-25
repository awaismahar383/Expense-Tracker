print('PERSONAL EXPENSE TRACKER')

def options():
    print("____________________________ ")
    print('1.Add expense')
    print('2.View expense')
    print('3.Total spending')
    print('4.spending by category')
    print('5.Search expense ')
    print('6.Delete expense ')
    print('7.Most expensive purchase')
    print('8.Exit: ')
    print("____________________________ ")
options()


expense = []
total_amount = 0


while True:
    options()
    user_choice = input("Enter your choice in numbers. ")
    
    if  user_choice == '1':
        Add_expense = int(input("Enter amount: "))
        category = input("Enter catogory: ")
        description = input("description: ")
        
        expense.append([Add_expense,category,description])
        
        total_amount = total_amount + Add_expense
    elif user_choice == '2':
        print(expense)
    elif user_choice == '3':
        print(total_amount)
    elif user_choice == '4':
        spending = {}

        for item in expense:
            amount = item[0]
            category = item[1]

            if category in spending:
                spending[category] += amount
            else: 
                spending[category] = amount
        
        print(spending)
    elif user_choice == '5':
        search = input("Enter your search: ")
        for item in expense:
            if search == item[1] or search == item[2]:
                print(item)
    elif user_choice == '6':
        
        print(expense)
        
        expense_delete = int(input("Which expense do you want to delete? Enter index: "))

        deleted_expense = expense.pop(expense_delete)

        total_amount -= deleted_expense[0]

        print("Expense deleted successfully!")
        
    
    
    elif user_choice == '7':
       
        if len(expense) == 0:
            print("no expese found.")
        
        else:
            amounts = []
            
            for item in expense:
                amounts.append(item[0])
                
            highest = max(amounts)
            highest_index =  amounts.index(highest)
                
            print(expense[highest_index])
    
    elif user_choice == '8':
        print('Exit')

        break        

            


        

        
    

            
    




    
    



        












    
    
    
    
 

    
    
