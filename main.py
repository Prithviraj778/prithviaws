from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import models,schemas
from . database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash



def get_db():
      db=SessionLocal()
      try:
            yield db
      finally:
            db.close()


################# initializing FastAPI  to app#############################
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

##################creating a user and adding to database

@app.post('/admin',status_code=status.HTTP_201_CREATED,tags=['Admin'])
def create(request:schemas.Admin,db : Session=Depends(get_db)):
      new_user=models.Admin(username=request.username,password=Hash.bcrypt(request.password),email_id=request.email_id,usertype=request.usertype,status=request.status, phoneno=request. phoneno)
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return new_user
#################### Displaying all users  ############################
@app.get('/admin',response_model=List[schemas.ShowAdmin],tags=['Admin'])
def all(db: Session=Depends(get_db)):
      users=db.query(models.Admin).all()
      return users


#############################  checking whether user is exisiting or not ###########################
@app.get('/admin/{id}', status_code=200,response_model=schemas.ShowAdmin,tags=['Admin'])
def show(id,response: Response,db: Session=Depends(get_db)):
      user=db.query(models.Admin).filter(models.Admin.email_id==id).first()
      if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{user} not existing")
            #response.status_code=status.HTTP_404_NOT_FOUND
            #return{'detail':f"{id} not existing"}
      #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{user.username} found")
      return user
#####################################        deleting a user ##################################

@app.delete('/admin/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['Admin'])
def destroy(id, db:Session=Depends(get_db)):
      user=db.query(models.Admin).filter(models.Admin.email_id==id)
      if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with{id} not found")
      user.delete(synchronize_session=False)
      db.commit()
      return 'Done'
      
@app.put('/admin/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Admin'])
def update(id, request:schemas.Admin,db:Session=Depends(get_db)):
      u=db.query(models.Admin).filter(models.Admin.email_id==id)
      if not u:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with{id} not found")
      u.update({'password':'Renuka@123'})
      db.commit()
      return 'Updated Sucessfully'

###########################GAT Hall tickets #############################

@app.post('/gat_applicant',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Gat_Application):
      return request

###########################GAT Call letter #############################
@app.post('/gat_call_letter', status_code=status.HTTP_201_CREATED ,tags=['Gat_Call_Letter'])
def create(request:schemas.Gat_call_letter,db:Session=Depends(get_db)):
    new_users=models.Gat_call_letter(
          fullname=request.fullname,
          appno=request.appno,
          email_id=request.email_id,
          mobileno=request.mobileno,
          gender=request.gender,
          gat_crtical=request.gat_crtical,
          gat_quant=request.gat_quant,
          gat_writing=request.gat_writing,
          gat_total=request.gat_total,
          gat_percentage=request.gat_percentage,
          psychometric_score=request.psychometric_score,
          gre_awa=request.gre_awa,
          gre_total=request.gre_total,
          toefl=request.toefl,
          ielts=request.ielts,
          exam_type=request.exam_type,
          rank=request.rank,
          cdate=request.cdate,
          ctime=request.ctime,
          gen_status=request.gen_status,
          email_status=request.email_status)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users
####################################### Generating GAT HALL tickets ###############################################
@app.get('/generate_callLetters',response_model=List[schemas.Gat_call_letter],tags=['Gat_Call_Letter'])
def all(db: Session=Depends(get_db)):
      users=db.query(models.Gat_call_letter).all()
      return users


####################################### Gat halltickets ###############################################

@app.post('/gat_hallticket',status_code=status.HTTP_201_CREATED,tags=['GatHalltickets'])
def create(request:schemas.GatHallticket,db : Session=Depends(get_db)):
      gat_user=models.GatHallticket(id=request.id,email_id=request.email_id,username=request.full_name,phoneno=request.mobile_no,image_url=request.image_url,gatAppNo=request.gatAppNo,center=request.center,examType=request.examType,paymentType=request.paymentType,paymentsStatus=request.paymentStatus,testDate=request.testDate,testTime=request.testTime,htStatus=request.htStatus,emailStatus=request.emailStatus,htTime=request.htTime,emailTime=request.emailTime)
      db.add(gat_user)
      db.commit()
      db.refresh(gat_user)
      return gat_user

@app.get('/generate_GatHallticket',response_model=List[schemas.GatHallticket],tags=['GatHalltickets'])
def all(db: Session=Depends(get_db)):
      users=db.query(models.GatHallticket).all()
      return users
    
   
   
   
    

         
  

    
    
     
