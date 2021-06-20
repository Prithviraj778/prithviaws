from sqlalchemy import Column,Integer,String
from .database import Base


class Admin(Base):
      __tablename__='external_users'
      username=Column(String(50))
      password=Column(String(150))
      email_id=Column(String(50),primary_key=True,index=True)
      usertype=Column(String(50))
      status=Column(String(50))
      phoneno=Column(String(50))
     
      
      
class Gatcallletter(Base):
      __tablename__='gat_call_letter'
      id=Column(Integer)
      fullname=Column(String(50))
      appno=Column(String(50))
      email_id=Column(String(50),primary_key=True,index=True)
      mobileno=Column(String(50))
      gender=Column(String(50))
      gat_crtical=Column(String(50))
      gat_quant=Column(String(50))
      gat_writing=Column(String(50))
      gat_total=Column(String(50))
      gat_percentage=Column(String(50))
      psychometric_score=Column(String(50))
      gre_awa=Column(String(50))
      gre_total=Column(String(50))
      toefl=Column(String(50))
      ielts=Column(String(50))
      exam_type=Column(String(50))
      rank=Column(String(50))
      cdate=Column(String(50))
      ctime=Column(String(50))
      gen_status=Column(String(50))
      email_status=Column(String(50))
      
      
class GatHallticket(Base):
      __tablename__='gat_halltickets'
      id = Column(Integer)
      email_id=Column(String(50),primary_key=True,index=True)
      username=Column(String(50))
      phoneno=Column(String(50))
      image_url=Column(String(150))
      gatAppNo=Column(String(20))
      center=Column(String(50))
      examType=Column(String(50))
      paymentType=Column(String(50))
      paymentsStatus=Column(String(50))
      testDate=Column(String(50))
      testTime=Column(String(50))
      htStatus=Column(String(50))
      emailStatus=Column(String(50))
      htTime=Column(String(50))
      emailTime=Column(String(50))
      
     
      
      

