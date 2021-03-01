import bcrypt
from password_validator import PasswordValidator


class Password():
    def __init__(self):
        self.schema = PasswordValidator()
        self.schema.min(8).max(100).has().digits().has().uppercase().has().lowercase().has().no().spaces()
        return

    def genHash(self, passw):
        return bcrypt.hashpw(passw.encode(), bcrypt.gensalt())

    def checkHash(self, passw, hash):
        return bcrypt.checkpw(passw.encode(), hash)

    def checkPasswordIsValid(self, passw):
        return self.schema.validate(passw)


if __name__ == "__main__":
    p = Password()
    k = p.genHash("peepeepoopoo")
    print(p.checkHash("peepeepoopoo", k))
