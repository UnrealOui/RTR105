ftext = open("testtext.txt")
for line in ftext:
    if line.startswith("X-DSPAM-Confidence:"):
       print(line)
print("Average spam confidence: ", cip)
