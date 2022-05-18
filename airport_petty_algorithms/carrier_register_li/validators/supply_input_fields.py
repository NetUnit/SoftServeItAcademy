class FuelArrivedField:
    '''
        ===========================================================
        This class represents a 'Fuel Supply Input'
        ===========================================================
        Attrs:
            :param msg2: error message for inappropriate field input
            :type msg: <str>
            :raises: ValueError when not int, float input & handles
            exception with a custom message
            
        .. note::
            get_classname() - aims to get cuurent classname when 
            exceptions raised. Inherited by following field classes.
    '''

    msg = 'Please enter a correct amount'
    msg2 = 'shoud be digits or 0 if no supply'
    fuel_arrived = None

    def __init__(self):
        try:
            self.fuel_arrived = int(
                input(
                    'Enter the fuel supply, kg: '
                    )
                )
        except (TypeError, AttributeError):
            # LOGGER.error(self.msg)
            print(self.msg)
        except ValueError:
            field_name = self.__class__.__name__
            msg3 =  self.get_classname(field_name)
            # LOGGER.error(f'{msg3} {self.msg2}')
            print(f'{msg3} {self.msg2}')
        finally:
            exit() if self.fuel_arrived is None else True
    
    @staticmethod
    def get_classname(field_name):
        field_name = ' '.join(
            re.findall(
                '[A-Z][^A-Z]*',
                field_name
            )
        ).capitalize()
        return field_name


class FuelResidueField(FuelArrivedField):
    '''
        ===========================================================
        This class represents a 'Fuel Arrived Input'
        ===========================================================
        Attrs:
            :param msg2: error message for inappropriate field input
            :type msg: <str>
            :raises: ValueError when not int, float input & handles
            exception with a custom message
    '''

    fuel_residue = None
    def __init__(self, prev_rep_date=None):
        try:
            self.fuel_residue = int(
                input(f'Insert fuel residue (kg) ' + 
                f'to date {prev_rep_date} 23:59: ')
            )
        except (TypeError, AttributeError):
            # LOGGER.error(self.msg)
            print(self.msg)
        except ValueError:
            field_name = self.__class__.__name__
            msg3 =  self.get_classname(field_name)
            # LOGGER.error(f'{msg3} {self.msg2}')
            print(f'{msg3} {self.msg2}')
        finally:
            exit() if self.fuel_residue is None or prev_rep_date is None else True


class FuelPickupField(FuelArrivedField):
    '''
        ===========================================================
        This class represents a 'Fuel Pickup Input'
        ===========================================================
        Attrs:
            :param msg2: error message for inappropriate field input
            :type msg: <str>
            :raises: ValueError when not int, float input & handles
            exception with a custom message
    '''

    fuel_pickup = None
    def __init__(self):
        try:
            self.fuel_pickup = int(
                input(
                    'Enter the fuel pickup trucks/railroad tanks, kg: '
                    )
                )
        except (TypeError, AttributeError):
            # LOGGER.error(f'{msg3} {self.msg2}')
            print(self.msg)
        except ValueError:
            field_name = self.__class__.__name__
            msg3 =  self.get_classname(field_name)
            # LOGGER.error(f'{msg3} {self.msg2}')
            print(f'{msg3} {self.msg2}')
        finally:
            exit() if self.fuel_pickup is None else True
