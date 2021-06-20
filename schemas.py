from pydantic import BaseModel

class Admin(BaseModel):
      username:str
      password:str
      email_id:str
      usertype:str
      status:str
      phoneno:str
      

class ShowAdmin(BaseModel):
      username:str
      email_id:str
      class Config():
            orm_mode=True



## 1.1 to see paramertes after execution we use pydantic model

class Gatcallletter(BaseModel):
      fullname:str
      appno:str
      email_id:str
      mobileno:str
      gender:str
      gat_crtical:str
      gat_quant:str
      gat_writing:str
      gat_total:str
      gat_percentage:str
      psychometric_score:str
      gre_awa:str
      gre_total:str
      toefl:str
      ielts:str
      exam_type:str
      rank:str
      cdate:str
      ctime:str
      gen_status:str
      email_status:str
      
      
class ShowGatcallletter(BaseModel):
      fullname:str
      appno:str
      email_id:str
      mobileno:str
      gender:str
      gat_crtical:str
      gat_quant:str
      gat_writing:str
      gat_total:str
      gat_percentage:str
      psychometric_score:str
      gre_awa:str
      gre_total:str
      toefl:str
      ielts:str
      exam_type:str
      rank:str
      cdate:str
      ctime:str
      gen_status:str
      email_status:str
      class Config():
            orm_mode=True
     
      
     


      



