
// enzyme code

query
https://www.brenda-enzymes.org/enzyme.php?ecno=6.4.1.2


plantNames = "planta, plantb"


queryKCat(6.4.1.2, plantNames)


function queryKCat(String enzymeCode, List<String> plantNames) {
	// open website
	https://www.brenda-enzymes.org/enzyme.php?ecno="enzymeCode"

	// search for plants
	for (plantName : plantNames) {
		// hit?
		return hit
		else return null
	}
}
