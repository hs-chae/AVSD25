class Label:
    def __init__(self, name, candidates):
        self.name = name
        self.candidates = candidates

empty_label     = Label('empty_label', [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",
                                    " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",])

capitals        = Label('capitals', ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
                                "Q","R","S","T","U","V","W","X","Y","Z"])

nums            = Label('nums', ["1","2","3","4","5","6","7","8","9","0","","","","","","","","","","",""])

capitalnum      = Label('capitalnum', [i + j for i in capitals.candidates for j in nums.candidates])

small_letters   = Label('small_letters', ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                                "q","r","s","t","u","v","w","x","y","z"])#, "", "", "", "", "", "", "", "", "", ""])

colors          = Label('colors', ["black"])

diverse_colors  = Label('colors', ["red","blue","green","orange","purple","pink","brown","black"])

angle_letters   = Label('angle_letters', [i + j for i in  small_letters.candidates for j in ["","°"]])

