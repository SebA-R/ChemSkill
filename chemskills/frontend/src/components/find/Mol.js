Molar_mass = { "n": 1.00866491597, "H": 1.00794, "He": 4.002602, "Li": 6.941, "Be": 9.012182, "B": 10.811, "C": 12.0107, "N": 14.0067, "O": 15.9994, "F": 18.9984032, "Ne": 20.1797, "Na": 22.98977, "Mg": 24.305, "Al": 26.981538, "Si": 28.0855, "P": 30.973761, "S": 32.065, "Cl": 35.453, "Ar": 39.948, "K": 39.0983, "Ca": 40.078, "Sc": 44.95591, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961, "Mn": 54.938049, "Fe": 55.845, "Co": 58.9332, "Ni": 58.6934, "Cu": 63.546, "Zn": 65.409, "Ga": 69.723, "Ge": 72.64, "As": 74.9216, "Se": 78.96, "Br": 79.904, "Kr": 83.798, "Rb": 85.4678, "Sr": 87.62, "Y": 88.90585, "Zr": 91.224, "Nb": 92.90638, "Mo": 95.94, "Tc": 98, "Ru": 106.90447, "Xe": 131.293, "Cs": 132.90545, "Ba": 137.327, "La": 138.9055, "Ce": 140.116, "Pr": 140.90765, "Nd": 144.24, "Pm": 145, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25, "Tb": 158.92534, "Dy": 162.5, "Ho": 164.93032, "Er": 167.259, "Tm": 168.93421, "Yb": 173.04, "Lu": 174.967, "Hf": 178.49, "Ta": 180.9479, "W": 183.84, "Re": 186.207, "Os": 190.23, "Ir": 192.217, "Pt": 195.078, "Au": 196.96655, "Hg": 200.59, "Tl": 204.3833, "Pb": 207.2, "Bi": 208.98038, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.0381, "Pa": 231.03588, "U": 238.02891, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 262, "Rf": 261, "Db": 262, "Sg": 266, "Bh": 264, "Hs": 277, "Mt": 268, "Ds": 281, "Rg": 272, "Cn": 285, "Nh": 286, "Fl": 289, "Mc": 289, "Lv": 293, "Ts": 294, "Og": 294 }
Elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
    "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru",
    "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce",
    "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
    "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut",
    "Fl", "Uup", "Lv", "Uus", "Uuo"]
function findMol() {
    let elm = Math.floor(Math.random() * 118);
    let m1 = Molar_mass[Elements[elm]] * (Math.floor(Math.random() * 5) + 1) + Math.floor(Math.random() * 40) + 1;

    let ans = m1 / Molar_mass[Elements[elm]];
    ans = Math.round(ans * 10) / 10;

    let user_input = parseFloat(prompt("How many mols of " + Elements[elm] + " are present if there is " + m1 + "g? (round to the tenth decimal place)"));

    if (user_input === ans) {
        alert("Correct");
    } else {
        alert("Incorrect, the answer is: " + ans + " mols.");
    }
}

if (window.location.href.endsWith("find-mol")) {
    while (true) {
        findMol();
    }
}
