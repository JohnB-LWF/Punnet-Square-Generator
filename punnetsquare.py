"""Simple Punnett square generator and offspring calculator.
File: punnetsquare.py
Inputs: 
1. Parent 1 Genotype
2. Parent 2 Genotype
3. Dominant Phenotype Name
4. Recessive Phenotype Name
Outputs:
1. 2x2 Punnett Square of offspring genotypes
2. The percentages of Phenotypes in the offspring (ex. 50% Hairy, 50% Not Hairy)
3. The percentage of offspring heterozygous for the dominant phenotype
"""

def read_single_character(prompt):
	"""Read a non-empty single-character allele symbol."""
	while True:
		value = input(prompt).strip()
		if len(value) == 1:
			return value
		print("Please enter exactly one character.")


def read_genotype(prompt, dominant_allele, recessive_allele):
	"""Read and validate a two-allele genotype (for example: Hh, hh)."""
	allowed = {dominant_allele, recessive_allele}
	while True:
		genotype = input(prompt).strip()
		if len(genotype) != 2:
			print("Genotype must be exactly 2 characters (example: Hh).")
			continue

		if any(allele not in allowed for allele in genotype):
			print(
				f"Genotype can only contain '{dominant_allele}' or '{recessive_allele}'."
			)
			continue

		return genotype


def normalize_genotype(allele_a, allele_b, dominant_allele, recessive_allele):
	"""Return genotype in consistent order, with dominant allele first when mixed."""
	pair = [allele_a, allele_b]
	pair.sort(key=lambda ch: 0 if ch == dominant_allele else 1)
	return "".join(pair)


def print_punnett_square(parent1, parent2, dominant_allele, recessive_allele):
	"""Build and print a 2x2 Punnett square and return offspring genotypes."""
	p1_gametes = [parent1[0], parent1[1]]
	p2_gametes = [parent2[0], parent2[1]]

	offspring = []
	for g1 in p1_gametes:
		row = []
		for g2 in p2_gametes:
			row.append(normalize_genotype(g1, g2, dominant_allele, recessive_allele))
		offspring.append(row)

	headers = [" ", p2_gametes[0], p2_gametes[1]]
	rows = [
		[p1_gametes[0], offspring[0][0], offspring[0][1]],
		[p1_gametes[1], offspring[1][0], offspring[1][1]],
	]

	col_widths = []
	for col_idx in range(3):
		max_len = len(headers[col_idx])
		for row in rows:
			max_len = max(max_len, len(row[col_idx]))
		col_widths.append(max_len)

	def format_row(values):
		return " | ".join(values[i].ljust(col_widths[i]) for i in range(3))

	separator = "-+-".join("-" * width for width in col_widths)

	print("\nPunnett Square")
	print(format_row(headers))
	print(separator)
	for row in rows:
		print(format_row(row))

	return [offspring[0][0], offspring[0][1], offspring[1][0], offspring[1][1]]


def calculate_phenotype_percentages(
	offspring,
	dominant_allele,
	recessive_allele,
	dominant_phenotype,
	recessive_phenotype,
):
	"""Calculate dominant/recessive phenotype percentages from offspring genotypes."""
	dominant_count = sum(1 for genotype in offspring if dominant_allele in genotype)
	recessive_count = len(offspring) - dominant_count
	hetero_genotype = f"{dominant_allele}{recessive_allele}"
	hetero_count = sum(1 for genotype in offspring if genotype == hetero_genotype)

	dominant_percent = (dominant_count / len(offspring)) * 100
	recessive_percent = (recessive_count / len(offspring)) * 100
	hetero_percent = (hetero_count / len(offspring)) * 100

	print("\nPhenotype Percentages")
	print(f"{dominant_percent:.0f}% {dominant_phenotype}")
	print(f"{recessive_percent:.0f}% {recessive_phenotype}")
	print(f"{hetero_percent:.0f}% may be heterozygous ({hetero_genotype})")


def main():
	print("Punnett Square Calculator (Single Gene)")

	dominant_allele = read_single_character(
		"Enter dominant allele symbol (example: H): "
	)
	recessive_allele = read_single_character(
		"Enter recessive allele symbol (example: h): "
	)

	while recessive_allele == dominant_allele:
		print("Dominant and recessive symbols must be different.")
		recessive_allele = read_single_character(
			"Enter recessive allele symbol (example: h): "
		)

	parent1 = read_genotype(
		"Enter Parent 1 genotype (example: Hh): ",
		dominant_allele,
		recessive_allele,
	)
	parent2 = read_genotype(
		"Enter Parent 2 genotype (example: hh): ",
		dominant_allele,
		recessive_allele,
	)

	dominant_phenotype = input("Enter dominant phenotype name (example: Hairy): ").strip()
	recessive_phenotype = input(
		"Enter recessive phenotype name (example: Not Hairy): "
	).strip()

	if not dominant_phenotype:
		dominant_phenotype = "Dominant Trait"
	if not recessive_phenotype:
		recessive_phenotype = "Recessive Trait"

	offspring = print_punnett_square(
		parent1, parent2, dominant_allele, recessive_allele
	)
	calculate_phenotype_percentages(
		offspring,
		dominant_allele,
		recessive_allele,
		dominant_phenotype,
		recessive_phenotype,
	)


if __name__ == "__main__":
	main()
