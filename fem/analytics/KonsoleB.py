#analytic solution for displacements
#Bernulli beam, constant bending moment, constant shear force
def dispKonsole(e, sect, load, L):
    sect.calc_geom()
    [F, Iy, Iz, Ip, Wy, Wz, Wp, Sy, Sz] = sect.get_g()
    [N, Qy, Qz, My, Mz, Mx] = load
    u = N / F / e.get_E() * L
    v = Qy * L**3 / 3 / e.get_E() / Iz + Mz * L**2 / 2 / e.get_E() / Iz
    w = Qz * L**3 / 3 / e.get_E() / Iy - My * L**2 / 2 / e.get_E() / Iy
    ty = My / e.get_E() / Iy * L - Qz * L**2 / 2 / e.get_E() / Iy
    tz = Mz / e.get_E() / Iz * L + Qy * L**2 / 2 / e.get_E() / Iz
    tx = Mx * L / e.get_G() / Ip
    return [u, v, w, ty, tz, tx]
