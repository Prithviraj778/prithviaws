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
            
class GatHallticket(BaseModel):
      id:int
      email_id:str
      full_name:str
      mobile_no:str
      image_url:str
      gatAppNo:str
      center:str
      examType:str
      paymentType:str
      paymentStatus:str
      testDate:str
      testTime:str
      htStatus:str
      emailStatus:str
      htTime:str
      emailTime:str
      pass
      
class ShowGatuser(BaseModel):
      username:str
      email_id:str
      gatAppNo=str
      class Config():
            orm_mode=True      





class Gat_Application(BaseModel):
      hall_ticket:str
      email_id:str

class Gat_call_letter(BaseModel):
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


class show_Gat_call_Letter(BaseModel):
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
