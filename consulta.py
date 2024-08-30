import janus_swi as janus

# Load the updated Prolog knowledge base
janus.consult("exemplo10.pl")

def herbivoro(X):
    # Check if the animal exists in the knowledge base
    resp1 = janus.query_once(f"animal({X})")
    if not resp1['truth']:
        print("Animal não existe na base")
        return
    
    # Query the Prolog knowledge base to determine if the animal is a herbivore
    resp2 = janus.query_once(f"herbivoro({X})")
    if resp2['truth']:
        print("Ele é herbívoro")
    else:
        print("Não é herbívoro")

# Main loop for user interaction
continuar = True
while continuar:
    animal = input("Animal: ")
    herbivoro(animal)
    resp = input("Continua? (s/n): ")
    continuar = (resp.lower() == "s")
