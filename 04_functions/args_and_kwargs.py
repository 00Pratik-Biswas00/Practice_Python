def func_args(*args):
    return sum(args)

print(func_args(2,3,5)) # tuple

def func_args_manual(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

print(func_args_manual(2,3,5))



def func_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

func_kwargs(fname="Pratik")
func_kwargs(fname="Pratik", sname = "Biswas")
func_kwargs(fname="Pratik", midname = "jesus christ", sname = "Biswas")
