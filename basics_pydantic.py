from pydantic import BaseModel,Field,computed_field
from typing import Literal

class Patient(BaseModel):
    name:str=Field(...,description="Enter the name")
    city:str=Field(...,description="Enter the address")
    age:int=Field(...,gt=0,lt=120,description="Enter the age")
    gender:Literal['male','female','other']=Field(...,description="Enter the gender")
    height:float=Field(...,gt=0,le=2.72,description="Enter the height(m)")
    weight:float=Field(...,gt=0,le=635,description="Enter the weight(kg)")
    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)

    @computed_field
    @property
    def verdict(self)->str:
         if self.bmi<18:
              return "underweight"
         elif self.bmi>=18 and self.bmi<=25:
              return "Normal"
         else:
              return "overweight"



patient1=Patient(**{"name":"damini","city":"Aligarh","age":"30","gender":"female","height":1.62,"weight":85})


def main(patient:Patient):
        print(patient.name)
        print(patient.city)
        print(patient.age)
        print(patient.gender)
        print(patient.height)
        print(patient.weight)
        print(patient.bmi)
        print(patient.verdict)
main(patient1)