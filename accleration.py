
#a function to find acceleration

def calc_acceleration(v, u, t):
    return (v - u) / t


final_velo = 25
init_velo = 0
time = 10

accln = calc_acceleration(final_velo, init_velo, time)

print("The required acceleration for initial velocity {:d}m/s, final velocity {:d}m/s and time {:d}sec is {:.3f}m/s^2.".format(init_velo, final_velo, time, accln))
