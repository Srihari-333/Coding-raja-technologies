tasks = []

def main():
    print("\n\n\t\t\tby @JATOTH ADITHYA NAIK")
    print("________________________________________")
    print("\n\t\t\t***TO DO LIST APP***\n") 
    while True :
        
        print("1.ADD")
        print("2.DELETE")
        print("3.VIEW")
        print("4.UPDATE")
        print("5.EXIT")
       
        choice=int(input("Enter your choice : "))
        print("\n")
        
        
       
        if(choice == 1):
            # taking the task from the user
            item = input("Enter the task that you wanna add : ")
            # adding the task to the tasks list with add(item) function
            add(item)
            
       
        elif(choice == 2):
           
            if(len(tasks)>0):
                print("YOUR TO DO TASKS : ")
                for i in range(len(tasks)):
                    print(f"{i+1}."+tasks[i])
                print("NOTE THAT INDEXING STARTS FROM '1' ONLY")
                index = int(input("Enter the index of the Task that you wanna delete :"))
               
                delete(index)
            else:
                print("No Tasks to remove\n")
                
       
        elif(choice == 3):
            
            show()
            
       
        elif(choice == 4):
            print("YOUR TO DO TASKS : ")
            for i in range(len(tasks)):
                print(f"{i+1}."+tasks[i])
            print("NOTE THAT INDEXING STARTS FROM '1' ONLY")
            index = int(input("Enter the index of the Task that you wanna update :")) 
           
            update(index)
            
       
        elif(choice == 5):
            print("Saving & Exiting ......\n")
            break;
        
       
        else:
            print("Enter valid input , please try again..\n")




def add(new_item):
    tasks.append(new_item)
    print("Added Task Successfully!!\n")
    print("________________________________________")


def delete(ind):
        tasks.pop(ind-1)
        print("Removed Task Successfully!!\n")
        print("________________________________________")
        

def show():
    if(len(tasks)==0):
         print("No Tasks to show\n")
    else:
        print("YOUR TASKS:")
        for i in range(len(tasks)):
            print(i+1,end=".")
            print(tasks[i])
        print("Shown your Tasks Succesfully!!\n")
    print("________________________________________") 
    
    

def update(ind):
    tasks.pop(ind-1)
    upd_task=input("Enter your new task : ")
    tasks.insert(ind-1,upd_task)
    print("Updated Task Successfully!!\n")
    print("________________________________________")


if __name__ == "__main__":
    main()
