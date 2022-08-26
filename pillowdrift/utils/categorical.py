from scipy.stats import chisquare

def chisquaretest(values_reference, values_current, threshold=0.95):
    _, pvalue = chisquare(values_current, values_reference)
    if pvalue < 1 - threshold:
        verdict = "not detected"
    else:
        verdict = "detected"

    return verdict, round(pvalue, 5)


def frequency_filter(labels, values_ref, values_cur, top=5):
    top = top - 1
    labels = [x for x, _ in sorted(zip(labels, values_ref), key=lambda pair: pair[0])]
    values_cur = [x for x, _ in sorted(zip(values_cur, values_ref), key=lambda pair: pair[0])]
    values_ref = sorted(values_ref)
    return labels[:top], values_ref[:top], values_cur[:top]


def categorical_frequency(labels, val_ref, val_cur):
    percentages_ref = []
    percentages_cur = []
    labels_map = {}
    for i, lab in enumerate(labels):
        labels_map[lab] = i

    for lab in labels:
        nb_ref = sum([1 if element == labels_map[lab] else 0 for element in val_ref ])
        nb_cur =  sum([1 if element == labels_map[lab] else 0 for element in val_cur])
        percentages_ref.append(nb_ref)
        percentages_cur.append(nb_cur)
    verdict, pvalue = chisquaretest(percentages_ref, percentages_cur, threshold=0.95)
    #verdict, pvalue = "no", 0.123
    val_ref = [element/sum(percentages_ref) for element in percentages_ref]
    val_cur = [element/sum(percentages_cur) for element in percentages_cur]

        
    return labels, val_ref, val_cur, verdict, pvalue


def categorical_data(data_reference, data_current, columns, config):
    categorical = list(config['model']['variables']['categorical'].keys())
    labels = list(config['model']['variables']['categorical'].values())

    categorical_elements = []
    for val_ref, val_cur, col in zip(data_reference, data_current, columns):
        if col in categorical:
            idx = categorical.index(col)
            lab = labels[idx]
            lab, val_ref, val_cur, verdict, pvalue = categorical_frequency(lab, val_ref, val_cur)
            lab, val_ref, val_cur = frequency_filter(lab, val_ref, val_cur, top=5)
            lab = [str(element) for element in lab]
            name = "Variable: {} <br> Data drift: {} <br> P-value: {}".format(col, verdict, pvalue)
            element = (name, lab, val_ref, val_cur)
            categorical_elements.append(element)

    return categorical_elements


def categorical_distribution_sampler(input_categorical_elements):
    categorical_elements = []
    for element in input_categorical_elements:
        name = element[0]
        labels = element[1]
        val_ref = element[2]
        val_cur = element[3]
        # Compute the chisquere test, retrieve the p-value and the verdict
        
        # Compute the KS test, retrieve the p-value and the verdict
        
        categorical_elements.append((name, labels, val_ref, val_cur, 'categorical'))
    return categorical_elements
