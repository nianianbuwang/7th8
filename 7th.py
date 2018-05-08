import numpy as np

K=0
flag=0

func = input('请输入函数：')
def fun(x):
    return eval(func)

a=float(input('请输入a:'))
b=float(input('请输入b:'))
sigma=float(input('请输入sigma：'))



while flag== 0:
    if fun(a)*fun(b)>0:
        print ("no anser")
        break
    elif fun(a)*fun(b)==0:
        if fun(a)==0:
           print ("result",a,K)
           flag=1
        else:
           print ("result",b,K)
           flag=1
    else:

        m=0.5*a+0.5*b
        if np.fabs(b-a)<sigma:
            print("result",m,K)
        else:
            if fun(a) * fun(m) > 0:
                a = m
            else:
                b = m
            K=K+1
