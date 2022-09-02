#!/usr/bin/python3


print("digraph hal_nets {")
print("""


graph [
rankdir = "LR"
];
node [
fontsize = "8"
];


""")

# defs
f = open("pin.out", "r")

component_hash={}

for line in f:
        comp_name, pin_type, pin_dir, pin_value, pin_name = line.split()[:5]
        if comp_name not in component_hash:
                component_hash[comp_name] = [];
        component_hash[comp_name].append(pin_name)

for comp in list(component_hash.keys()):
        comp_labels = ["<" + c + "> " + c for c in component_hash[comp]]
        print(("\"" + comp + "\"" + " ["))
        print(("\tlabel = " + "\"" + " | ".join(comp_labels) + "\""))
        print("\tshape = \"record\"")
        print("]")
        print("\n\n\n")

# nets


def component(component_hash,pin):
        for lst in list(component_hash.values()):
                if pin in lst:
                        return list(component_hash.keys())[list(component_hash.values()).index(lst)]



f = open("pin.out", "r")

net_list = []

for line in f:
        sig_list = line.split()
        sig_type, sig_value = sig_list[0:2]
        sig_declarations = sig_list[2:]
        for count in range(len(sig_declarations)):
                if sig_declarations[count] in ["<==", "==>"]:
                        pin1 = sig_declarations[count - 1]
                        pin2 = sig_declarations[count + 1]

                        comp1 = component(component_hash, pin1)
                        if comp1 != None:
                                comp1 = "\"" + comp1 + "\"" + ":"
                        else:
                                comp1 = ""
                        comp2 = component(component_hash, pin2)

                        if comp2 != None:
                                comp2 = "\"" + comp2 + "\"" + ":"
                        else:
                                comp2 = ""

                        comp_pin1 = comp1 + "\"" + pin1 + "\""
                        comp_pin2 = comp2 + "\"" + pin2 + "\""

                        if sig_declarations[count] == "<==":
                                net_list.append(comp_pin2 + " -> " + comp_pin1) # "a <== b" ===>> "b -> a"
                        if sig_declarations[count] == "==>":
                                net_list.append(comp_pin1 + " -> " + comp_pin2) # "a ==> b" ===>> "a -> b"

for line in net_list:
        print((line + ";"))

print("}")
