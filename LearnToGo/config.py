#configuring db
class Config:
  #setting debug to be true to have live updates on terminal
  DEBUG=True
  SQLALCHEMY_DATABASE_URI='sqlite:///words.db'
