# Beginners_Python_Tools

These tools were created to perform simple tasks. Written in order to practice python at a beginners level.

#BMI calculator example

```print 'The simple BMI Calculator!'

weight=float(input('What is your weight in kg? '))
height=float(input('What is your height in Metres? '))
BMI=weight/(height*height)

if BMI<=18.5:
    print 'Your body mass index is', BMI , 'this is classed as underweight'
elif BMI>18.5 and BMI<=25:
    print 'Your body mass index is', BMI ,'this is classed as weight'
elif BMI>25 and BMI<=30:
    print 'Your body mass index is', BMI ,'this is classed as overweight'
elif BMI>30:
    print 'Your body mass index is', BMI ,'this is classed as obese'
else:
    print 'There was an error with your input'

print 'Thank you for using the simple BMI Calculator'
```
