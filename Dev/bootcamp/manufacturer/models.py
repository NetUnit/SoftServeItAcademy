from django.db import models, IntegrityError, DataError
from django.forms.models import model_to_dict
from django.http.response import Http404

# Create your models here.
class Manufacturer(models.Model):

    '''
        This class represents the manufacturer of a certain product \n
        -----------------------------------------------------------
        Attrs:
        param name: Describes the comapny name
        type: str max_length = 40
        param country: Depicts the manufacturer's country of origin
        type: str max_length = 20
        param year: depicts the foundation year year of a company
        type: date

        NOTE: Manufacturer model is more customized than Product
            in order to avoid less code in views
    '''

    title = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=20, blank=True)
    year = models.DateField()

    class Meta:
        ordering = ('id',) 

    # def __str__(self):
    #     '''
    #         This magic method is created  in order to show all
    #         info about a class Manufacturer
    #         :return manufacturer.id,  manufacturer.name,  manufacturer.country,  manufacturer.year

    #     '''
    #     # return str(self.to_dict())[1:-1]
    #     #return Manufacturer
    #     return f'{self.id} {self.title} {self.country} {self.year}'

    
    def __repr__(self):
        '''
            This megic method is redefined in order to show class name and id 
            of a certain product object
            :return: class, id
        '''
        return f'{self.__class__.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(manufacturer_id):
        '''
            This method is created in order to get manufacturer object
            found in the DB
            :return Manufacturer object or None if such a manufacturer does not exist in the DB
            (None will raise 404 status)
        '''
        try:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            return manufacturer 
        except Manufacturer.DoesNotExist:
            raise Http404
            # LOGGER.error("Manufacturer does not exist")
    
    @staticmethod
    def get_all():
        '''
            This method is created in order to get a queryset of all present objects
            found in the DB
            :return Manufacturer queryset of all objects or empty list if nothing has been found
            in the DB
        '''
        try:
            manufacturers = Manufacturer.objects.all()
            return list(manufacturers)
        except Manufacturer.DoesNotExist:
            raise Http404
            # LOGGER.error("Manufacturers does not exist")

    @staticmethod
    def delete_by_id(manufacturer_id):
        '''
            This method is created in order to delete manufacturer object
            found in the DB
            :return True if such an object was found in the DB or False if it didn't existed
        '''
        try:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            manufacturer.delete()
            return True
        except Manufacturer.DoesNotExist:
            pass
        return False
            # LOGGER.error("User does not exist")
    
    @staticmethod
    def create(title, country, year):
        '''
            This method is created in order to create manufacturer object
            to be saved into a DB
            param name: Describes the comapny name
            type: str max_length = 40
            param country: Depicts the manufacturer's country of origin
            type: str max_length = 20
            param year: depicts the foundation year of a company
            type: date
        '''
        try:
            manufacturer = Manufacturer.objects.create(title=title, country=country, year=year)
            manufacturer.save()
            return manufacturer 
        except(IntegrityError, DataError, AttributeError):
            pass
            # LOGGER.error("User does not exist")
    
    @staticmethod
    def update_by_id(manufacturer_id, title=None, country=None, year=None):
        '''
            This method is created in order to update manufacturer object
            :params: same as in create method, if param is None - no update done
            :return None
        '''
        try:
            manufacturer = Manufacturer.get_by_id(manufacturer_id)
            update_data = {
                    'title': title,
                    'country': country,
                    'year': year
                    }
            manufacturer.__dict__.update(**update_data)
            manufacturer.save()
            return manufacturer

        except Exception as error:
            print(error)
            return False
            
