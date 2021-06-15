from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")
class Hash():
      def bcrypt(self:str):
            hashedPassword=pwd_cxt.hash(self)
            return hashedPassword
