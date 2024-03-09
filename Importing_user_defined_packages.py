from Object_oriented.Packages import Hello,add

print(Hello.Hello(),"Did you know that summation of 1, 2 is :",add.addition_between_two_integers(1,2),"?")

import Object_oriented.Packages.A_class_under_packages as A # Object_oriented is a package that has a Package called Package that has a python file called A_class_under_packages
                                                            # A_class is the class name and state_your_package_info() is it's method
                                                            
print(A.A_class.state_your_package_info()) # No wonder Java is verbose, think about, there is a package under a package which contains a java file that has a class that has a method 
                                           # just like this program,  maybe that's why java's class name and java file name is same