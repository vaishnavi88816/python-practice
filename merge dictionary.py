#1st method
d1={10:100,20:200,30:300,40:400}
d2={50:500,60:600,70:700,80:800}
d1.update(d2)
print("merge dictionary is:-",d1)
#2nd method using for loop
d1={10:100,20:200,30:300,40:400}
d2={50:500,60:600,70:700,80:800}
for i in d2:
    d1[i]=d2[i]
print("merge dictionary is:-",d1)
