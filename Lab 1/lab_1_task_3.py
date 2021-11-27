import math as solve
import basic as calc
class s_calc(calc.basic_calc):
    def fact(self):
        num1 = self.val1
        num2 = self.val2
        val1 = val2 = 1
        while 1:
            val1 *= num1
            num1 -= 1
            if num1 == 0:
                break
        while 1:
            val2 *= num2
            num2 -= 1
            if num2 == 0:
                break
        return s_calc(val1, val2)
    def power(self):
        x = self.val1
        y = self.val2
        x_power_y = x**y
        y_power_x = y**x
        return s_calc(x_power_y, y_power_x)
    def log(self):
        x = self.val1
        y = self.val2
        log_x_base_y = solve.log(x, y)
        log_y_base_x = solve.log(y, x)
        return s_calc(log_x_base_y, log_y_base_x)
    def ln(self):
        x = self.val1
        y = self.val2
        ln_x = solve.log(x)
        ln_y = solve.log(y)
        return s_calc(ln_x, ln_y)
    
bcalc = calc.basic_calc(10, 5)
scalc = s_calc(bcalc.val1, bcalc.val2)
print("\nbasic_calc Starts Here!\n")
print(f"Addition   of {bcalc} = {bcalc.sum()}")
print(f"Difference of {bcalc} = {bcalc.subt()}")
print(f"Division   of {bcalc} = {bcalc.div()}")
print(f"Product    of {bcalc} = {bcalc.prod()}")
print("\ns_calc Starts Here!\n")
print(f"Product of {scalc} = {scalc.fact()}")
print(f"Power   of {scalc} = {scalc.power()}")
print(f"Log     of {scalc} = {scalc.log()}")
print(f"ln      of {scalc} = {scalc.ln()}")
input()
