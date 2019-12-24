import pickle

example_dict = {"sharad":"2","data1":"3","data3":"data"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
