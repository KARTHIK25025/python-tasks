from fastapi import FastAPI,HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine,Column,Integer,String,Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
app=FastAPI()
# ------------------------------------------------------------
# 🗄️ Database Configuration# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:Root@localhost:3306/student_db"
 
 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
 
Base = declarative_base()
# DataBaseModel(Table)
class stdDb(Base):
    __tablename__="StudentManagementSystem"
    id=Column(Integer,primary_key=True,index=True)
    name= Column(String(100))
    age=Column (Integer)
    Course= Column(String(100))
    marks=Column(Float)
    completed = Column(Boolean, default=False)
#Creating Table
Base.metadata.create_all(bind=engine)
# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Std(BaseModel):
    id: int
    name: str
    age: int
    Course: str
    marks: float
    completed: bool = False
 
    class Config:
        orm_mode = True
 
# ------------------------------------------------------------
# 🔌 Dependency (DB Session)
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
@app.get("/")
def home():
    return {"message":"Student Fastapi  DB"}
# ------------------------------------------------------------
# ✅ 1. CREATE TODO
# ------------------------------------------------------------
 
@app.post("/std_info/")
def create_std(std:Std,db:Session = Depends(get_db) ):
    existing = db.query(stdDb).filter(stdDb.id == std.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="ID already exists")
    new_std = stdDb(
        #id=std.id,
        name=std.name,
        age=std.age,
        Course=std.Course,
        marks=std.marks,
        completed=std.completed
    )
 
    db.add(new_std)
    db.commit()
    db.refresh(new_std)
 
    return {"message": "STD_MANAGEMENT created", "data": new_std}
 
# ------------------------------------------------------------
# ✅ 2. READ ALL TODOS
# ------------------------------------------------------------
@app.get("/STD")
def get_all_std(db:Session = Depends(get_db)):
    stds = db.query(stdDb).all()
    return {"count": len(stds), "data": stds}
 
# ------------------------------------------------------------
# ✅ 3. READ SINGLETODO
# ------------------------------------------------------------
@app.get("/std/{std_id}")
def get_std(std_id: int, db: Session = Depends(get_db)):
    std = db.query(stdDb).filter(stdDb.id == std_id).first()
 
    if not std:
        raise HTTPException(status_code=404, detail="STUDENT not found")
 
    return std
# ------------------------------------------------------------
# ✅ 4. UPDATETODO
# ------------------------------------------------------------
 
@app.put("/std/{std_id}")
def update_std(std_id: int, updated: Std, db: Session = Depends(get_db)):
    std = db.query(stdDb).filter(stdDb.id == std_id).first()
 
    if not std:
        raise HTTPException(status_code=404, detail="Todo not found")
 
    std.name = updated.name
    std.age = updated.age
    std.Course = updated.Course
    std.marks = updated.marks
       
 
    std.completed = updated.completed
 
    db.commit()
    db.refresh(std)
 
    return {"message": "Updated successfully", "data": std}
# ------------------------------------------------------------
# ✅ 5. DELETE TODO
# ------------------------------------------------------------
@app.delete("/std/{std_id}")
def delete_todo(std_id: int, db: Session = Depends(get_db)):
    std = db.query(stdDb).filter(stdDb.id == std_id).first()
 
    if not std:
        raise HTTPException(status_code=404, detail="Student not found")
 
    db.delete(std)
    db.commit()
 
    return {"message": "Deleted successfully"}