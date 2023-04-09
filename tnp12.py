'''def selection_sort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])
data=[20,12,10,15,2]
size=len(data)
selection_sort(data,size)
print("sorted array in ascending order")
print(data)'''
#Question 1
'''class employee:
    def __init__(self,name,basic_salary,qualification):
        self.name=name
        self.basic_salary=basic_salary
        self.qualification=qualification
    def validate_salary(self):
        if self.basic_salary>3000:
            return True
        else:
            return False
    def validate_qualification(self):
        if self.qualification=="Bachelors" or self.qualification== "master":
            return True
        else:
            return False
class graduate(employee):
    def __init__(self,name,basic_salary,qualification,job_band,cgpa):
        employee.__init__(self,name,basic_salary,qualification)
        self.job_band=job_band
        self.cgpa=cgpa
    def validate_job_band(self):
        j_b=["A","B","C"]
        if self.job_band in j_b:
            return True
        else:
            return False
    def cal_gross_salary(self):
        if self.validate_salary and self.validate_qualifiacation and self.validate_job_band:
            pf=0.12*self.basic_salary
            if self.cgpa>=4 and self.cgpa<=4.254:
                tpi=1000
            elif self.cgpa>=4.26 and self.cgpa<=4.5:
                tpi=1700
            elif self.cgpa>=4.51 and self.cgpa<=4.75:
                tpi=3200
            else:
                tpi=5000
            if self.job_band=="A":
                incentive=0.04*self.basic_salary
            elif self.job_band=="B":
                incentive=0.06*self.basic_salary
            else:
                incentive=0.10*self.basic_salary
            gross_salary=self.basic_salary+pf+tpi+incentive
            return gross_salary
        else:
            return -1
class lateral(employee):
    def __init_(self,name,basic_salary,qualification,job_band,skill_set):
        super().__init__(name,basic_salary,qualification)
        self.job_band=job_band
        self.skill_set=skill_set
    def validate_job_band(self):
        j_b=["D","E","F"]
        if self.job_band in j_b:
            return True
        else:
            return False
    def cal_gross_salary(self):
        if self.validate_basic_salary and self.validate_qualifiacation and self.validate_job_band:
            pf=0.12*self.basic_salary
            if self.skill_set=="AGP":
                SME_Bonous=6500
            elif self.skill_set=="AGPT":
                SME_Bonous=8200
            elif self.skill_set=="AGDEV":
                SME_Bonous=11500
            else:
                return -1
            if self.job_band=="D":
                incentive=0.13*self.basic_salary
            elif self.job_band=="E":
                incentive=0.16*self.basic_salary
            else:
                incentive=0.20*self.basic_salary
            gross_salary=self.basic_salary+pf+SME_Bonous+incentive
            return gross_salary
        else:
          return -1   
    
x=graduate("ranjeeta",5000,"master","A",4.5)
print("details")
print("name",x.name)
print("basic_salary",x.cal_gross_salary)'''
'''def partn(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partn(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
data=[8,7,6,1,0,9,2]
print("unsorted data")
high=len(data)
quicksort(data,0,high-1)
print(data)'''
'''x=input()
y=[]
y=x.split()
freq=[y.count(i) for i in y]
print(dict(zip(y,freq)))'''
#question 2
'''def freq(text):
    a={}
    for i in text.lower().split():
        if i not in a:
            a[i]=1
        else:
            a[i]+=1
    max_freq=0
    max_freq_word=""
    for word in a:
        if a[word]>max_freq:
            max_freq=a[word]
            max_freq_word=word
        elif a[word]==max_freq:
            if len(word)>len(max_freq_word):
                max_freq_word=word
    return max_freq_word+" "+str(max_freq)

print(freq("Good bad bad good summer"))'''

#question 3

'''def chk_anagram(x,y):
    if sorted(x)==sorted(y):
        print("anagram")
    else:
        print("not anagram")
chk_anagram("eat","tae")'''
            
    


            




            
        
        
