def decor_result(result_function): #Ye return krega dist
    def dist(marks):
        for m in marks:
            if m>=75:
                print("Congrats YOu HAve distinction in",m)
        else:
            result_function(marks)# 3) fir again result call hoga
    return dist    #2)fir ye chlega or dist call hoga

@decor_result #always call decorator weather pass or fail



def result(marks):
    for i in marks:
        if i>=33:
            pass
        else:
            print("Fail")
            break
    else :
        print("Pass")
result([33,88,99,77,25,68,97,1])        
        
