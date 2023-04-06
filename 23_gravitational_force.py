def grav_force (mass1, mass2, radius) :
    G = (6.67) * (10 ** -11)

    g_force = ((G * mass1 * mass2) / (radius ** 2))


    return f'Gravitational Force: {g_force:.5}' # round (g_force, 4) will do the same



mass_1 = float (input ("Enter mass one: "))
mass_2 = float (input ("Enter mass two: "))
radius = float (input ("Enter radius (Distance between objects): "))

print (grav_force (mass_1, mass_2, radius))