class Assertion:
    def __init__(self, block_from, block_yes, block_no):
        # Block that contains the test (assertion)
        self.block_from = block_from

        # Block that is executed when the assertion is true
        self.block_yes = block_yes

        # Block that contains INVALID
        # This block should fall to INVALOD
        self.block_no = block_no

        # Was the assertion violated?
        self.violated = False

        # If the assertion was violated,
        # store the counterexample
        self.model = None

        # SMT2 query to decide the assertion
        self.query = None

        # Solidity function that might contain this assertion
        self.function = None

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def get_block_from(self):
        return self.block_from

    def get_block_yes(self):
        return self.block_yes
    
    def get_block_no(self):
        return self.block_no

    def is_violated(self):
        return self.violated

    def set_violated(self, violated):
        self.violated = violated

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_query(self):
        return self.query

    def set_query(self, query):
        self.query = query

    def __str__(self):
        s =  "================\n"
        s += "Assertion from block " + str(self.block_from) + "\n"
        s += "SMT2 query:\n" + str(self.query) + "\n"
        s += "Violated: " + str(self.violated) + "\n"
        s += "In function: "
        if self.function == None:
            s += "?\n"
        else:
            s += self.function + "\n"
        if self.violated:
            s += "Model:\n"
            for decl in self.model.decls():
                s += str(decl.name()) + " = " + str(self.model[decl]) + ", "
        return s

    def display(self):
        print self.__str__()

