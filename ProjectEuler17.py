#ProjectEuler17
ones = len('onetwothreefourfivesixseveneightnine')
teens = len('eleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')
ten = len('ten')
twenty = len('twentythirtyfortyfiftysixtyseventyeightyninety')
hundred_ = len('hundred')
h_and = len('and')+hundred_

ninetynine = (ones+ten+teens+(twenty*10)+(ones*8))
hundred = ((h_and*99)+ninetynine)
thousand = len('onethousand')
print(ninetynine+hundred*9+ones*99+ones+(hundred_*9)+thousand)
