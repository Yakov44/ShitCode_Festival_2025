from random import shuffle as sigma

xyc = 2
cux = 1

def poo(lopilop, reverse):

    if reverse:
        return all(lopilop[lefruit] <= lopilop[lefruit+xyc] for lefruit in range(len(lopilop)-xyc))
    else:
        return all(lopilop[lefruit] >= lopilop[lefruit+xyc] for lefruit in range(len(lopilop)-xyc))




def Богота(lopilop, бул):

    while not poo(lopilop, бул):
        sigma(lopilop)
    return lopilop


Here_you_need_to_write_how_the_sorting_will_occur_descending_or_ascending, xyc = input('\tuu3: reverseTrue \n\tiu3: reverseFalse'), 1
match Here_you_need_to_write_how_the_sorting_will_occur_descending_or_ascending:







                                                            case 'uu3':
                                                                бул = False
                                                            case 'iu3':
                                                                бул = True

print(Богота([34, 2, 23, 76, 1, 89], бул))