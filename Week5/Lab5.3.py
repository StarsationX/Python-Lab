def quantity():
    q = int(input("Total Item Quantity <<< "))
    psum = 0.0
    for i in range(q):
        p = float(input(f"Item #{i+1} Price <<< "))
        psum += p
    return psum

# W Optimization wtf

psum = quantity()

print("\nTotal Price (w/o Vat) >>> %.2f" % psum)
print("Vat >>> %.2f" % (psum * (7/100)))
print("Total Price (with Vat) >>> %.2f" % (psum * 1.07))