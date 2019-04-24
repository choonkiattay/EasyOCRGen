import numpy as np


class LicensePlate(object):

    def __init__(self, number):
        # print("License Plate")
        self.vlp_list = []
        self.dict = [class_name.rstrip('\n') for class_name in open('generators/dictionary')]
        # For distribute the number of plate type
        self.a = int(number * 0.15)
        self.ab = int(number * 0.15)
        self.abc = int(number * 0.15)
        self.a_a = int(number * 0.15)
        self.ab_a = int(number * 0.15)
        self.abc_a = int(number * 0.10)
        self.special_ = int(number * 0.05)
        self.diplomatic_ = int(number * 0.1)
        self.limo_ = int(number * 0.0001)

    def number_prop(self, plate_amount):
        # To make sure the distribution of license plate, Probability of digits number as below
        # Total number of digits combination = 10000 ; 1 to 9999
        # 1 to 9 = 9/10000
        prob_1digit = int(plate_amount * 0.001)
        prop_2digit = int(plate_amount * 0.009)
        prop_3digit = int(plate_amount * 0.09)
        prop_4digit = int(plate_amount * 0.9)
        prop_list = [prob_1digit, prop_2digit, prop_3digit, prop_4digit]
        return prop_list

    def prefix1(self,):
        char = str(self.dict[np.random.randint(10, 36)])
        return char

    def prefix2(self,):
        char = str(self.dict[np.random.randint(10, 36)])
        char += str(self.dict[np.random.randint(10, 36)])
        return char

    def prefix3(self,):
        char = str(self.dict[np.random.randint(10, 36)])
        for j in range(2):
            char += str(self.dict[np.random.randint(10, 36)])
        return char

    def special(self,):
        special = str(self.dict[np.random.randint(62, 108)])
        return special

    def limo__(self,):
        limo = str(self.dict[np.random.randint(108, 109)])
        return limo

    def digits(self, num):
        digit = None
        if num == 0:
            digit = str(self.dict[np.random.randint(0, 10)])
        elif num == 1:
            digit = str(self.dict[np.random.randint(0, 10)])
            digit += str(self.dict[np.random.randint(0, 10)])
        elif num == 2:
            digit = str(self.dict[np.random.randint(0, 10)])
            for j in range(2):
                digit += str(self.dict[np.random.randint(0, 10)])
        elif num == 3:
            digit = str(self.dict[np.random.randint(0, 10)])
            for j in range(3):
                digit += str(self.dict[np.random.randint(0, 10)])
        return digit

    def one_prefix(self, ):
        plate_1prx = []
        amount_gen = self.a
        plate_distribution = self.number_prop(amount_gen)
        print("A Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.prefix1()
                digit = self.digits(j)
                plate = pfx + ' ' + digit
                plate_1prx.append(plate)
        return plate_1prx

    def two_prefix(self, ):
        plate_1prx = []
        amount_gen = self.ab
        plate_distribution = self.number_prop(amount_gen)
        print("AB Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.prefix2()
                digit = self.digits(j)
                plate = pfx + ' ' + digit
                plate_1prx.append(plate)
        return plate_1prx

    def three_prefix(self, ):
        plate_1prx = []
        amount_gen = self.abc
        plate_distribution = self.number_prop(amount_gen)
        print("ABC Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.prefix3()
                digit = self.digits(j)
                plate = pfx + ' ' + digit
                plate_1prx.append(plate)
        return plate_1prx

    def prefix_post1(self, ):
        plate_1prx = []
        amount_gen = self.a_a
        plate_distribution = self.number_prop(amount_gen)
        print("A_A Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.prefix1()
                ptfx = self.prefix1()
                digit = self.digits(j)
                plate = pfx + ' ' + digit + ' ' + ptfx
                plate_1prx.append(plate)
        return plate_1prx

    def prefix_post2(self, ):
        plate_1prx = []
        amount_gen = self.ab_a
        plate_distribution = self.number_prop(amount_gen)
        print("AB_A Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.prefix2()
                ptfx = self.prefix1()
                digit = self.digits(j)
                plate = pfx + ' ' + digit + ' ' + ptfx
                plate_1prx.append(plate)
        return plate_1prx

    def prefix_post3(self, ):
        plate_1prx = []
        amount_gen = self.abc_a
        plate_distribution = self.number_prop(amount_gen)
        print("ABC_A Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.prefix3()
                ptfx = self.prefix1()
                digit = self.digits(j)
                plate = pfx + ' ' + digit + ' ' + ptfx
                plate_1prx.append(plate)
        return plate_1prx

    def special_prefix(self, ):
        plate_1prx = []
        amount_gen = self.special_
        plate_distribution = self.number_prop(amount_gen)
        print("Special Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.special()
                digit = self.digits(j)
                plate = pfx + ' ' + digit
                plate_1prx.append(plate)
        return plate_1prx

    def limo(self,):
        plate_1prx = []
        amount_gen = self.limo_
        plate_distribution = self.number_prop(amount_gen)
        print("Limo Distribution: {0}".format(plate_distribution))
        for j in range(len(plate_distribution)):
            for k in range(plate_distribution[j]):
                pfx = self.limo__()
                ptfx = self.prefix1()
                digit = self.digits(j)
                plate = pfx + ' ' + digit + ' ' + ptfx
                plate_1prx.append(plate)
        return plate_1prx

    def plate(self, ):
        p_a = self.one_prefix()
        p_ab = self.two_prefix()
        p_abc = self.three_prefix()
        p_a_a = self.prefix_post1()
        p_ab_a = self.prefix_post2()
        p_abc_a = self.prefix_post3()
        p_special = self.special_prefix()
        p_limo = self.limo()
        total = p_a + p_ab + p_abc + p_a_a + p_ab_a + p_abc_a + p_special + p_limo
        return total

    # TODO: Philippine license plate
