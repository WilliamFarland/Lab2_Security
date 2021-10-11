from RSA import generate_keypair, encrypt, decrypt

p = 1297273  # Get your P value from the excel file
q = 1297651  # Get your P value from the excel file

# Part 1 - Generate the public, private keypair
public, private = generate_keypair(p, q)
print("RSA Public Key pair = " + str(public))
print("RSA Private Key pair = " + str(private))

