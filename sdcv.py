smean, ssd, size, pmean, sig = 22, 3, 16, 20, 0.05
z = ((size**0.5)*(smean-pmean))/ssd
t = 1.753

print("The table value of t is :", t, " and the calculated value of z is : ", round(z,3));
if z > t:
    print("Null hypothesis is rejected as Z is in the rejection region, therefore the new model has a higher mileage")
else:
    print("Null hypothesis is not rejected")
