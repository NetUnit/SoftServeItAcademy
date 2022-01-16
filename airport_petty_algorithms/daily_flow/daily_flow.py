class CalculateFuel:
  UTN_JET = {
    'st_res': 89325,
    'flow': [8480, ]
    }
  UTN_RT = {    
    'st_res': 536410,
    'flow': [4103, 1926, 1950,
             10375, 481, 2333]
    }
  AMIC_JET = {
    'st_res': 293896,
    'flow': [4408, 5942, 3557]
  }
  OKKO_JET = {
    'st_res': 20985,
    'flow': [724, 4687,]
  }

  LUX_RT = {
    'st_res': 194998,
    'flow': [1202, ]
  }
  
  
  # kwargs should be key UTN_JET: object
  def __init__(self, *args, kwargs={
                  'UTN_JET': UTN_JET,  
                  'UTN_RT': UTN_RT,
                  'AMIC_JET': AMIC_JET,
                  'OKKO_JET': OKKO_JET,
                  'LUX_RT': LUX_RT
                  }
              ):
    attr = args[0] if bool(args) else []
    self.attr = kwargs.get(str(attr))
    self.args = args
    new_dict = dict()
    for key, value in kwargs.items():
      if bool(value):
        new_dict[key] = value
    self.kwargs = new_dict
    self.number = sum(
      [len(i.get('flow')) for i in kwargs.values()]
      ) if bool(self.kwargs) else 0

  def calculate_sep(self, *args, **kwargs):
    st_res = self.attr.get('st_res')
    flow = self.attr.get('flow')
    for value in flow:
      st_res -= value
      print(st_res)
    return ''


  def calculate(self, *args):
    # print(args)
    # args = args[0] if len(args)>0 else ['']
    if self.kwargs == None:
        raise TypeError('No attrs to calculate')
    if args:
        company = ''.join([i[0] for i in args])
        data = [i[1] for i in args]
        data_exist = bool(data)
        data = data[0] if data_exist else dict()
        flow = data.get('flow')
        st_res = data.get('st_res')
        print(f'Вхідний залишок по {company}: {st_res}')
        for value in flow:
          st_res -= value
          print(f'-{value}={st_res}')
    return ''
  
  def calculate_total(self, *args):
    # args = args[0] if len(args)>0 else ['']
    if self.kwargs == None:
      raise TypeError('No attrs to calculate')
    if args:
        company = ''.join([i[0] for i in args])
        data = [i[1] for i in args]
        data_exist = bool(data)
        data = data[0] if data_exist else dict()
        flow = data.get('flow')
        num =  self.doc_num(data)
        print(f'Тотал по: `{company}` --> {sum(flow)}. {num}')
    return ''

  def calculate_all(self):
     items = list(self.kwargs.items())
     result = list(map(lambda x: self.calculate(x), items))
     return print(result)
     
  def calculate_total_all(self):
    items = list(self.kwargs.items())
    result = list(map(lambda x: self.calculate_total(x), items))
    return print(result)

  def doc_num(self, data=None):
    return (
      'Кількість вимог: ' +
      str(len(data.get('flow')))
    )

  def doc_num_all(self, obj=None):
    return print(
      'Загальна кількість вимог: ' +
      str(self.number)
    )

  #def doc_num(self):
    #return (
      #'кількість вимог: ' +
      #str(len(self.attr.get('flow')))
    #)

  def test_attr(self):
    attr = f"self.attr: {self.attr}"
    kwargs = f"self.attr: {self.kwargs}"
    return print(attr)
    
if __name__ == "__main__":
  inst = CalculateFuel()
  # inst.calculate()
  # inst.get_total()
  # inst.doc_num()
  # inst.calculate_sep()
  inst.calculate_all()
  inst.calculate_total_all()
  inst.doc_num_all()
  # inst.test_attr()