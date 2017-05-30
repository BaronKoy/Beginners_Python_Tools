#5 day avergae blood pressure calculator v.1.0
#created 30/05/2016, Baron Koylass

#Calculating systolic pressure
n=1
while n>0:
    in1=raw_input('Please enter your systolic pressure measured on day 1: ')
    in2=raw_input('Please enter your systolic pressure measured on day 2: ')
    in3=raw_input('Please enter your systolic pressure measured on day 3: ')
    in4=raw_input('Please enter your systolic pressure measured on day 4: ')
    in5=raw_input('Please enter your systolic pressure measured on day 5: ')
    n=n-1
    try:
        systo1=float(in1)
        systo2=float(in2)
        systo3=float(in3)
        systo4=float(in4)
        systo5=float(in5)
    except:
        print 'Invalid input-please enter systolic pressure as number value'
        continue
systolic=(systo1+systo2+systo3+systo4+systo5)/5
print 'Thank you for your systolic pressure input'

#Calculating diastolic pressure
x=1
while x>0:
    ip1=raw_input('Please enter your diastolic pressure measured on day 1: ')
    ip2=raw_input('Please enter your diastolic pressure measured on day 2: ')
    ip3=raw_input('Please enter your diastolic pressure measured on day 3: ')
    ip4=raw_input('Please enter your diastolic pressure measured on day 4: ')
    ip5=raw_input('Please enter your diastolic pressure measured on day 5: ')
    x=x-1
    try:
        diasto1=float(ip1)
        diasto2=float(ip2)
        diasto3=float(ip3)
        diasto4=float(ip4)
        diasto5=float(ip5)
    except:
        print 'Invalid input-please enter diastolic pressure as number value'
        continue
diastolic=(diasto1+diasto2+diasto3+diasto4+diasto5)/5


#Output of calculations and typing of blood pressure group
print 'Thank you, your blood pressure reading over the last 5 days is', systolic,'/',diastolic

if systolic<120 and diastolic<80:
    print 'This level falls into the Normal blood pressure group, maintain or adopt a healthy lifestyle. '
elif systolic>=120 and systolic<=139 and diastolic>=80 and diastolic<=89:
    print 'This level falls into the Prehypertension blood pressure group, maintain or adopt a healthy lifestyle.'
elif systolic>=140 and systolic<=159 and diastolic>=90 and diastolic<=99:
    print 'This level falls into the Stage 1 hypertension blood pressure group, maintain or adopt a healthy lifestyle. If your blood pressure goal is not reached in about a month, talk to your doctor about taking one or more medications.'
elif systolic>=160 and diastolic>=100:
    print 'This level falls into the Stage 2 hypertension blood pressure group, maintain or adopt a healthy lifestyle. Talk to your doctor about taking more than one medication.'
else:
    print 'The measures between systolic and diastolic pressure do not seem to be in the correct ranges, please check your readings again'

print 'Thank you for using the 5 day blood pressure calculator'
