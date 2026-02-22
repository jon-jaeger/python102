#============ Class = US_State ========
# Defining the class template for US_State
class US_State:

    # constructor
    # we use this to create a new object
    def __init__(self, a_name, a_capitol, a_flower, a_bird):
        self.name = a_name
        self.capitol = a_capitol
        self.flower = a_flower
        self.bird = a_bird
     
    #Double UNDERscore method = magic method
    # it will be called by Python behind scenes
    # DUNDER method
    def __str__(self):
        state_str =( '\n\nNAME : ' + self.name +
                    '\nCAPITOL : ' + self.capitol +
                    '\nFLOWER : ' + self.flower +
                    '\nBIRD: ' + self.bird )
        return state_str

    
      
# Create some objects
state_ca = US_State("California", "Sacremento", "Golden Poppy", "Quail")
print("Printing the California details")
print(state_ca)


state_mn = US_State("Minnesota", "St.Paul", "Lady Slipper", "Common Loon")
print("Printing the Minnesota details")
print(state_mn)
