while True: 
 num1= float(input("ادخل الرقم الاول : "))
 num2= float(input(" ادخل الرقم الثاني :"))
 print ("اختر العملية: ")
 print("للجمع +")
 print("للطرح -")
 print("للضرب *")
 print("للقسمة /")
 op= input  ("اكتب العملية هنا :")
 if op =="+":
     result = num1 + num2 
 elif op =="-":
     result = num1 - num2 
 elif op =="*":
     result = num1 * num2 
 elif op =="/":
     result = num1 / num2 

 else: print("عملية غير صحيحة")
 print("الناتج هو :", result)
 print("مقارنة الرقمين :")
 if  num1 > num2 :
  print("الرقم الاول اكبر من الرقم الثاني")
 elif  num1 < num2 :
  print("الرقم الاول اصغر من الرقم الثاني")

 else : print(" الرقم الاول يساوي الرقم الثاني")

 again = input ( "هل تريد تكرار العملية (نعم \لا): ")
 if again == "لا":
  break