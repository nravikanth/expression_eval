import json
from collections import namedtuple
data1 = {"user":{
		"address":{
			"address_line":"XYZ Street",
			"city":"San Francisco", 
			"state": "CA",
			"zipcode":"94150"
			},
		"age":40,
		},
	}

exp1=["AND",["EQ","user.address.city","San Francisco"],["LT", "user.age",55]]
exp2=["OR",["IN","user.address.state",["IND","DA","A"]],["LT","user.age",24]]

exp=exp2
class exp_eval(object):
	
	@classmethod
	def AND(cls, args):
		return reduce(lambda x,y: x and y, args)
			
	@classmethod
	def OR(cls, args):
		return reduce(lambda x,y: x or y, args)			
			
	@classmethod
	def EQ(cls, args):
		return args[0] == args[1]

	@classmethod
	def LT(cls, args):
		return args[0] < args[1]

	@classmethod
	def GT(cls, args):
		return args[0] > args[1]	
	
	@classmethod
	def IN(cls, args):
		return args[0] in args[1]

def get_value(args):
	return str([eval(args[0]), args[1]])

def get_object(data):
	json_data = json.dumps(data)
        vars()[data.keys()[0]]=json.loads(json_data, object_hook=lambda d: namedtuple(data.keys()[0],d.keys())(*d.values()))
        return eval(data.keys()[0]+'.'+data.keys()[0])


if __name__=='__main__':
	temp_list=[]
	# coverting the json data to python objects
	# if multiple json data, then same method can be used to get objects of json data
	vars()[data1.keys()[0]] = get_object(data1)
	for obj in exp[::-1][:-1]:		
		fun = "exp_eval."+obj[0]+"("+get_value(obj[1:])+")"
		temp_list = [eval(fun)] + temp_list
	fun= "exp_eval."+exp1[0]+"("+str(exp[:1]+temp_list)+")"
	print eval(fun)
