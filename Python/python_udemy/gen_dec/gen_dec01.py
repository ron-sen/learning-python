#generators and decorators ,
# instead of return it uses yield

def serve_chai():
     yield "Cup 1: Masala chai"
     yield "Cup 2: Ginger chai"
     yield "Cup 3: elacihi chai"


stall = serve_chai()

for cup in stall:
     print(cup)

def get_chai_gen():
     yield "Cup 1" 
     yield "Cup 2" 
     yield "Cup 3" 


chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai))  # will raise stop iteration error

