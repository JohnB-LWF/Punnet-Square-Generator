"""Utility functions for Streamlit Punnett Square Generator.
Contains core logic extracted from punnetsquare.py.
"""


def normalize_genotype(allele_a, allele_b, dominant_allele, recessive_allele):
    """Return genotype in consistent order, with dominant allele first when mixed."""
    pair = [allele_a, allele_b]
    pair.sort(key=lambda ch: 0 if ch == dominant_allele else 1)
    return "".join(pair)


def calculate_punnett_square(parent1, parent2, dominant_allele, recessive_allele):
    """Calculate offspring genotypes from parent genotypes.
    
    Returns a list of 4 offspring genotypes in the order:
    [top-left, top-right, bottom-left, bottom-right]
    """
    p1_gametes = [parent1[0], parent1[1]]
    p2_gametes = [parent2[0], parent2[1]]

    offspring = []
    for g1 in p1_gametes:
        for g2 in p2_gametes:
            offspring.append(
                normalize_genotype(g1, g2, dominant_allele, recessive_allele)
            )

    return offspring


def calculate_phenotype_percentages(
    offspring,
    dominant_allele,
    recessive_allele,
    dominant_phenotype,
    recessive_phenotype,
):
    """Calculate dominant/recessive phenotype percentages from offspring genotypes.
    
    Returns a dictionary with percentage information.
    """
    dominant_count = sum(1 for genotype in offspring if dominant_allele in genotype)
    recessive_count = len(offspring) - dominant_count
    hetero_genotype = f"{dominant_allele}{recessive_allele}"
    hetero_count = sum(1 for genotype in offspring if genotype == hetero_genotype)

    dominant_percent = (dominant_count / len(offspring)) * 100
    recessive_percent = (recessive_count / len(offspring)) * 100
    hetero_percent = (hetero_count / len(offspring)) * 100

    return {
        "dominant_percent": dominant_percent,
        "recessive_percent": recessive_percent,
        "hetero_percent": hetero_percent,
        "dominant_phenotype": dominant_phenotype,
        "recessive_phenotype": recessive_phenotype,
    }
