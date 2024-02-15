def add(n1,n2):
  if operator == "+":
   return n1 + n2

def sub(n1,n2):
  if operator == "-":
    return n1 - n2

def mul(n1,n2):
  if operator == "*":
    return n1 * n2

def div(n1,n2):
  if operator == "/":
    return n1 / n2

operations = {
  "+" : add,
  "-": sub,
  "*": mul,
  "/": div
}
def rec():
  n1 = float(input("what's the first number?: "))
  for symbals in operations:
    print(symbals)
    
  continue_1 = True
  while continue_1:
    operator = input("Pick an operation: ")
    n2 = float(input("what's the next number?: "))
    calculation = operations[operator]
    result_1 = calculation(n1,n2)
    print(f"{n1} {operator} {n2} = {result_1}")
    if input(f"Type 'y' to continue calculation with {result_1},or type 'n' to start new: ") == "y":
      n1 = result_1
    else:
      continue_1 = False
      rec()



rec()
