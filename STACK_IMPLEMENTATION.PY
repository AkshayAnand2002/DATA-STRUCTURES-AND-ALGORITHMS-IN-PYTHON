#Stack Implementation
def create_stack():
    stack=[]
    return stack
def check_empty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("PUSHED ELEMENT: "+item)
def pop(stack):
    if(check_empty(stack)):
        return "Stack is empty."
    return stack.pop()
stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("POPPED ITEM : "+ pop(stack))
print("STACK AFTER POPPING AN ELEMENT: "+ str(stack))
print(check_empty(stack))#GIVES FALSE AS STACK IS NOT EMPTY.
