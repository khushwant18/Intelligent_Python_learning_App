from  matplotlib import pyplot as plt
import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
class Evaluation:

    def add_Score(self,marks=[],name='Sanket'):
        """ add_score function will be use to add user's score csv file which can be processed to evaluate the performance """
        score=0
        l=[]
        #Score calculation
        for i in marks:
          if i==1:
           score+=1
        if score<3:
          print("Fail")
        x=[1,2,3,4]
        for i in marks:
            l.append([name,i,1])
        df=pd.DataFrame(l)
        df.to_csv('report.csv', mode='a',index=False, header=False)
        p=self.performance()
        plt.text(1.2,1,'Your performance is ='+str(np.round(p,2)))
        plt.plot(x,marks,'g--')
        plt.xlabel("Level")
        plt.ylabel("Score")
        plt.show()
        


    def get_Results(self):
        """ get_Results() function is used to evaluate the users performance on the basis of scores"""
        y=[]
        with open ('report.csv', 'r')as mf:
          mycsv=csv.reader(mf)
          for row in mycsv:
              text=row[-1]
              y.append(row[-1])
        print(y)
        sum=0
        for num in y:
          sum += int(num)
        print(sum)
        avg=sum/10
        if avg<6.5:
          print("You need to improve.")
        else:
          print("You are good to start coding.")
        x=[1,2,3,4,5,6,7,8,9,10]
        p=self.performance()
        plt.text(0.2,0.8,'Your performance is ='+str(np.round(p,2)))     
        plt.plot(x,y,'g--')
        plt.xlabel("Level")
        plt.ylabel("Score")
        plt.show()
        
    def performance(self):
        data = pd.read_csv('report.csv')
        x=data.iloc[:,[1]].values
        y=data.iloc[:,[2]].values
        data.head()
        lr = LinearRegression()
        lr.fit(x, y)
        pred=lr.predict(x)
        actual=x
        error=pred-actual
        summ=np.sum(error)
        degrade=(summ/len(actual))*100
        performance=100-degrade
        return performance