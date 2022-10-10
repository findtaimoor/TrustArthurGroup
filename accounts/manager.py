from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self,password=None, **extra_fileds):
        
        user = self.model(**extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,password,**extra_fileds):
        extra_fileds.setdefault('is_staff',True)
        extra_fileds.setdefault('is_superuser',True)
        extra_fileds.setdefault('is_active',True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))

        return self.create_user(password,**extra_fileds)