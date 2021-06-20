from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from reportlab.lib import styles
from . import schemas,models
from . database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash
from reportlab.pdfgen import canvas
from reportlab.lib import colors
##from reportlab.platypus import drawImage




def get_db():
      db=SessionLocal()
      try:
            yield db
      finally:
            db.close()


      
################# initializing FastAPI  to app#############################
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

##################creating a user and adding to database ##########

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


############################# checking whether user is exisiting or not ###########################
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

###########################GAT CALL #############################

# @app.post('/gat_applicant',status_code=status.HTTP_201_CREATED)
# def create(request:schemas.Gat_Application):
#       return request


@app.post('/gat_call_letter', status_code=status.HTTP_201_CREATED ,tags=['Gat_Call_Letter'])
def create(request:schemas.Gatcallletter,db:Session=Depends(get_db)):
    new_users=models.Gatcallletter(
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

@app.get('/gat_call_letter',response_model=List[schemas.ShowGatcallletter],tags=['Gat_Call_Letter'])
def all(db: Session=Depends(get_db)):
      users=db.query(models.Gatcallletter).all()
      fileName = 'callletter.pdf'
      documentTitle = 'Document title!'
      pdf = canvas.Canvas(fileName)
      ##..........title.........
      title = 'Consortium of Institutions of Higher Learning'
      pdf.setFont('Helvetica-Bold', 23)
      pdf.drawCentredString(300, 770, title)
      ##..........subtitle.........
      subTitle = 'IIIT Campus, Gachibowli,Hyderabad - 32, Phone:: 040-24001970 Mobile: 7799834583 / 84 / 85'
      pdf.setFillColorRGB(0, 0, 0)
      pdf.setFont("Helvetica-Bold", 11)
      pdf.drawCentredString(290,740, subTitle)
      ##..........line.........
      pdf.line(40, 720, 560, 720)
      ##..........textline.........
      textLines = [
    'Master of Science in Information Technology'
    ]
      text = pdf.beginText(170, 680)
      text.setFont("Helvetica-Bold", 13)
      text.setFillColor(colors.black)
      for line in textLines:
            text.textLine(line)
      pdf.drawText(text)
      ##..........call.........
      call=[
        'CALL LETTER'
    ]
      text = pdf.beginText(240, 630)
      text.setFont("Helvetica-Bold", 15)
      text.setFillColor(colors.black)
      for line in call:
            text.textLine(line)
      pdf.drawText(text)
      ##..........date.........
      date=[
        'Date:'
    ]
      text = pdf.beginText(500, 640)
      text.setFont("Helvetica-Bold", 11)
      text.setFillColor(colors.black)
      for line in date:
            text.textLine(line)

      pdf.drawText(text)
      ##..........image.........
      # Story=[]
      #im = Image('msit.JPEG', width=2*inch, height=2*inch)
      # im.hAlign = 'LEFT'
      # Story.append(im)


      
      #msit = 'msit.JPEG' 
      ##canvas.drawImage( 'msit.JPEG',60, 640,  width=110, height=39)
      # pdf.drawInlineImage(image, 60,640, width=110, height=39)
      
      ##..........a.........
      a=[
        'Dear Mr. / Ms.'
    ]
      text = pdf.beginText(60, 600)
      text.setFont("Helvetica-Bold", 11)
      text.setFillColor(colors.black)
      for line in a:
            text.textLine(line)

      pdf.drawText(text)
      ##..........b.........
      b=['Sub: MSIT 2020 - Counseling and Allotment of MSIT Learning Center,'
    ]
      text = pdf.beginText(60, 580)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in b:
            text.textLine(line)

      pdf.drawText(text)
      ##..........paragraph1.........
      paragraph1=['Thank You for completing the online counseling registration process. You are required to appear for',
                'the counseling for allotment of seat in MSIT Learning Center at IIITH/JNTUH/JNTUK/JNTUA/SVU',
                '(direct admission) at the following online zoom link on the date and time mentioned below. Allotment ',
                'of seats are as per the GAT/GRE ranks and subject to availability of seats in the learning centers.'
    ]
      text = pdf.beginText(60, 560)
      text.setFont("Helvetica", 11 )
      text.setFillColor(colors.black)
      for line in paragraph1:
            text.textLine(line)

      pdf.drawText(text)
      ##..........g.........
      g=['Online zoom link:'
    ]
      text = pdf.beginText(60, 500)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in g:
            text.textLine(line)

      pdf.drawText(text)
      ##..........h.........
      h=['Meeting ID                                 :'  
    ]
      text = pdf.beginText(60, 480)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in h:
            text.textLine(line)

      pdf.drawText(text)
      ##..........i.........
      i=['Meeting Password                    :'
    ]
      text = pdf.beginText(60,460 )
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in i:
            text.textLine(line)

      pdf.drawText(text)
      ##..........j.........
      j=['Date and Time                           :'    
    ]
      text = pdf.beginText(60, 440)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in j:
            text.textLine(line)

      pdf.drawText(text)
      ##..........k.........
      k=['MSIT Rank                                 :'    
    ]
      text = pdf.beginText(60, 420)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in k:
            text.textLine(line)

      pdf.drawText(text)
      ##..........l.........
      l=['Hall Ticket/Reference Number :'   
    ]
      text = pdf.beginText(60, 400)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in l:
            text.textLine(line)

      pdf.drawText(text)
      ##..........m.........
      m=['Admission fee paid                   : '   
    ]
      text = pdf.beginText(60,380 )
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in m:
            text.textLine(line)

      pdf.drawText(text)
      ##..........n.........
      n=['Admission fee paid                   : '   
    ]
      text = pdf.beginText(60,360 )
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in n:
            text.textLine(line)

      pdf.drawText(text)
      ##..........o.........
      o=['Date of payment                        : '
    ]
      text = pdf.beginText(60, 340)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in o:
            text.textLine(line)

      pdf.drawText(text)
      ##..........paragraph......... 
      paragraph =[
        'The balance amount of annual fee has to be paid after admissions on the reporting/induction day.',
        'The amount paid is non refundable, if admission is taken. Loan documents for bank loan purpose',
        'will be issued on the counseling day. Please join online counseling zoom link only in the',
        'specified time above (slot given to you).'
    ]
      text = pdf.beginText(60, 320)
      text.setFont("Helvetica", 11, )
      text.setFillColor(colors.black)
      for line in paragraph:
            text.textLine(line)

      pdf.drawText(text)
      ##..........date.........
      
      par=['For any reason if you are unable to participate in the counseling at scheduled slot/time then it will be',
        'considered as absent, counseling process will go on and the seat will be allotted to the next rank holder.',
        'Absentees can only obtain seats in the second phase of counseling, for the remaining/available seats as ',
        'per rank order.'
    ]
      
      text = pdf.beginText(60, 260)
      text.setFont("Helvetica-Bold", 10, )
      text.setFillColor(colors.black)
      for line in par:
            text.textLine(line)

      pdf.drawText(text)
      ##..........note.........
      note=['Note:'
    ]
      text = pdf.beginText(60, 195)
      text.setFont("Helvetica-Bold", 11, )
      text.setFillColor(colors.black)
      for line in note:
            text.textLine(line)

      pdf.drawText(text)
      ##..........points.........
      points=['1. If you are not able to secure seat as per GAT/GRE rank the amount of Rs.30,000 paid online will be',
				'    refunded.',
            '2. Please call help line numbers 7799834583, 7799834584, 7799834585 if you are having any difficulties',
                   '  during admissions process.',
            '3. The amount paid is non refundable, if admission is taken.', 
            '4. If you need training material on zoom meetings, please go through document at this link',
                            'https://bit.ly/30qKSCr'
    ]
      text = pdf.beginText(60, 180)
      text.setFont("Helvetica", 11, )
      text.setFillColor(colors.black)
      for line in points:
            text.textLine(line)

      pdf.drawText(text)
      ##..........leftimage.........
      # leftimage = 'sign.JPEG'
      # pdf.drawInlineImage(leftimage, 60, 70,  width=110, height=20)
      ##..........p.........
      p=['Dean,'
    ]
      text = pdf.beginText(60, 60)
      text.setFont("Helvetica", 11, )
      text.setFillColor(colors.black)
      for line in p:
            text.textLine(line)

      pdf.drawText(text)
      ##..........q.........
      q=['CIHL, MSIT Division,'
    ]
      text = pdf.beginText(60, 48)
      text.setFont("Helvetica", 11, )
      text.setFillColor(colors.black)
      for line in q:
            text.textLine(line)

      pdf.drawText(text)
      ##..........r.........
      r=['CIHL, MSIT Division,'
    ]
      text = pdf.beginText(60, 36)
      text.setFont("Helvetica", 11, )
      text.setFillColor(colors.black)
      for line in r:
            text.textLine(line)

      pdf.drawText(text)
      pdf.setTitle(documentTitle)
      pdf.save()
      return users
     